def update_dict_fields(fields, **fields_mapping):
    updated_fields = dict(fields)
    for k, v in fields.items():
        if k in fields_mapping:
            updated_fields[k] = fields_mapping[k]
    return updated_fields


def remove_dict_fields(d, *keys):
    return dict(filter(lambda f: f[0] not in keys, d.items()))
