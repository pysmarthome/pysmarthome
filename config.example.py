collections = {
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
    'db': {
        'bucket_name': 'pysmarthome',
    }
}
