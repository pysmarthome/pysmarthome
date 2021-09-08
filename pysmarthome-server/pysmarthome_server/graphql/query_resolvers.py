from ariadne import QueryType


query = QueryType()

def dev_ctrl_to_dict(ctrl):
    children_models = ctrl.model.children_models
    children_dicts = {}
    for k, models in children_models.items():
        if len(models) == 1:
            children_dicts[k] = models[0].to_dict()
        else:
            children_dicts[k] = []
            for model in models:
                children_dicts[k].append(model.to_dict())
    return {
        **ctrl.to_dict(),
        **children_dicts,
        'typename': ctrl.model_class.graphql_name,
    }


def plugin_to_dict(plugin):
    ctrls = plugin.controllers.values()
    return {
        **plugin.to_dict(),
        'devices': [dev_ctrl_to_dict(ctrl) for ctrl in ctrls],
    }


@query.field('plugin')
def resolve_plugin(_, info, id):
    g = info.context['g']
    return plugin_to_dict(g.plugin_manager.plugins[id])


@query.field('plugins')
def resolve_plugins(_, info):
    g = info.context['g']
    return [plugin_to_dict(p) for p in g.plugin_manager.plugins.values()]


@query.field('device')
def resolve_device(_, info, id):
    g = info.context['g']
    ctrls = g.plugin_manager.get_controllers()
    return dev_ctrl_to_dict(ctrls[id])


@query.field('devices')
def resolve_devices(_, info, type='', power=''):
    g = info.context['g']
    ctrls = g.plugin_manager.get_controllers().values()
    if type:
        ctrls = [ctrl for ctrl in ctrls if ctrl.model.graphql_name == type]
    if power:
        ctrls = [ctrl for ctrl in ctrls if ctrl.get_power() == power]
    return [dev_ctrl_to_dict(ctrl) for ctrl in ctrls]


@query.field('devices_info')
def resolve_devices_info(_, info):
    g = info.context['g']
    ctrls = g.plugin_manager.get_controllers().values()
    infos = {}
    for ctrl in ctrls:
        name = ctrl.model.graphql_name
        if name not in infos:
            fields = ctrl.model.schema_attrs.keys()
            infos[name] = {'ids': [], 'fields': fields}
        infos[name]['ids'].append(ctrl.id)
    return [{ 'type': k, 'ids': v['ids'], 'fields': v['fields'] }
        for k, v in infos.items()]
