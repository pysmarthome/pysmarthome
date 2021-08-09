config = {
    'port': 5000,
    'devices': {
        'broadlink': {
            'addr': '255.255.255.255',
            'tv': {
                'addr': '255.255.255.255',
                'commands': {
                    'vol_up': b'',
                    'vol_down': b'',
                    'mute': b'',
                    'toggle': b'',
                },
            },
            'floor_lamp': {
                'commands': {
                    'on': b'',
                    'off': b'',
                },
            },
            'ac': {
                'commands': {
                    'on': b'',
                    'off': b'',
                },
            },
        },
        'govee': {
            'FF:FF:FF:FF:FF:FF:FF:FF': 'dev_name_a',
            'FF:FF:FF:FF:FF:FF:FF:FF': 'dev_name_b',
            'FF:FF:FF:FF:FF:FF:FF:FF': 'dev_name_c',
            'FF:FF:FF:FF:FF:FF:FF:FF': 'dev_name_d',
        },
        'sonoff': {
            'lava_lamp': {
                'addr': '255.255.255.255',
            },
            'salt_lamp': {
                'addr': '255.255.255.255',
            },
        },
        'pc_lamp': {
            'addr': '255.255.255.255',
        },
        'pc': {
            'actions_handler_addr': '255.255.255.255:5001',
            'addr': '192.168.15.26',
            'mac_addr': 'FF:FF:FF:FF:FF:FF',
        },
    },
}
