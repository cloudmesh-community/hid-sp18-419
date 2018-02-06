DOMAIN = {
    'disks': {
        'item_title': 'disk',
        'resource_methods': ['GET'],
        'schema': {
            'platform': {
                'type': 'string',
                'minlength': 1,
                'maxlength': 100,
            },
            'disk_size': {
                'type': 'string',
                'minlength': 1,
                'maxlength': 15,
            },
            'disk_used': {
                'type': 'string',
                'minlength': 1,
                'maxlength': 15,
            },
            'disk_free': {
                'type': 'string',
                'minlength': 1,
                'maxlength': 15,
            },
            'disk_percent': {
                'type': 'string',
                'minlength': 1,
                'maxlength': 15,
            },
        },
    },
}
