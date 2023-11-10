from os import environ
from typing import Any, Callable
from functools import wraps
from flask import Response, request, make_response, jsonify

def flag_manager_check(cb_fun: Callable[..., Response]) -> Callable[..., Response]:
    @wraps(cb_fun)
    def wrapper(*args: Any, **kwargs: Any) -> Response:
        token = environ['FLAG_MANAGER_SECRET']
        expected_value = f"Bearer {token}"
        if request.headers.get('Authorization') != expected_value:
            response = {"message": "Unauthorized"}
            return make_response(jsonify(response), 401)

        return cb_fun(*args, **kwargs)

    return wrapper