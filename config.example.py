collections = {
    'configs_ref': 'configs_ref',
    'govee_config': 'govee_config',
    'broadlink_config': 'broadlink_config',
    'devices_ref': 'devices_ref',
    'acs': 'acs',
    'broadlink_lamps': 'broadlink_lamps',
    'govee': 'govee',
    'pcs': 'pcs',
    'sonoffs': 'sonoffs',
    'tvs': 'tvs',
    'yeelights': 'yeelights',
    'broadlink_commands': 'broadlink_commands',
    'pc_actions': 'pc_actions',
    'states': 'device_states',
}

ping_cmd = 'fping -c1 -t100'

config = {
    'port': 5000,
    's3db': {
        'bucket_name': 'pysmarthome',
        'encoding': 'json',
        'aws_access_key_id': '',
        'aws_secret_access_key': '',
        'cache': True,
        'collection_files': {
            'root': [
                collections['broadlink_config'],
                collections['govee_config'],
                collections['configs_ref'],
                collections['devices_ref'],
            ],
            'devices': [
                collections['tvs'],
                collections['acs'],
                collections['broadlink_lamps'],
                collections['yeelights'],
                collections['pcs'],
                collections['sonoffs'],
                collections['govee'],
            ],
            'device_states': [
                collections['states']
            ],
            'broadlink_commands': [
                collections['broadlink_commands']
            ],
            'pc_actions': [
                collections['pc_actions'],
            ],
        }
    }
}
