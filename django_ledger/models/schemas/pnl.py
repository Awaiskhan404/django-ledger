

SCHEMA_PNL_DATA = {
    'type': 'object',
}

SCHEMA_PNL = {
    'type': 'object',
    'properties': {
        'entity_slug': {
            'type': 'string'
        },
        'entity_name': {
            'type': 'string'
        },
        'pnl_data': SCHEMA_PNL_DATA
    },
    'required': [
        'entity_slug',
        'entity_name',
        'pnl_data'
    ]
}
