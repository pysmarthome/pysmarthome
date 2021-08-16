def get_base_classes(cls):
    r = [cls]
    for b in cls.__bases__:
        if b.__name__ != 'object':
            r.extend(get_base_classes(b))
    return r


def get_methods_in(*classes):
    r = []
    for cls in classes:
        methods = [(key, f) for key, f in cls.__dict__.items() if callable(f)]
        r.extend(methods)
    return r


def update_dict_fields(fields, **fields_mapping):
    updated_fields = dict(fields)
    for k, v in fields.items():
        if k in fields_mapping:
            updated_fields[k] = fields_mapping[k]
    return updated_fields
