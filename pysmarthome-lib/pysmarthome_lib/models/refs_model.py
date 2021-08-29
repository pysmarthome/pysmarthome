from vesla_pymvc import Model


class RefModel(Model):
    schema = {
        **Model.schema,
        'collection_id': {
            'type': 'string',
            'required': True,
        }
    }
