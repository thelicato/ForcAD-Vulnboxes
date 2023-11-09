login_or_register_schema = {
    'type': 'object',
    'properties': {
        'username': {'type': 'string'},
        'password': {'type': 'string'}
    },
    'required': ['username', 'password']
}

redeem_schema = {
    'type': 'object',
    'properties': {
        'coupon': {'type': 'string'}
    },
    'required': ['coupon']
}

put_flag_schema = {
    'type': 'object',
    'properties': {
        'id': {'type': 'string'},
        'name': {'type': 'string'},
        'description': {'type': 'string'},
        'value': {'type': 'string'},
        'image': {'type': 'string'},
        'price': {'type': 'integer'},
        'hash': {'type': 'string'}
    },
    'required': ['id', 'name', 'description', 'value', 'image', 'price', 'hash']
}