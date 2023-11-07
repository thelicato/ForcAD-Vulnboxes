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
