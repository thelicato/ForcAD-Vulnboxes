from typing import Any, Callable
from functools import wraps
from flask import Response, request, make_response, jsonify, session
import jsonschema
import app.logger as logger
import app.utils as utils


def auth_check(cb_fun: Callable[..., Response]) -> Callable[..., Response]:
    @wraps(cb_fun)
    def wrapper(*args: Any, **kwargs: Any) -> Response:
        user_id = session.get('user_id')

        if not user_id:
            response = {"message": "Unauthorized"}
            return make_response(jsonify(response), 401)
        return cb_fun(*args, **kwargs)

    return wrapper


def validate_json(cb_fun: Callable[..., Response]) -> Callable[..., Response]:
    @wraps(cb_fun)
    def wrapper(*args: Any, **kw: Any) -> Response:
        try:
            request.json
        except Exception as err:
            logger.error(
                f"""Error for {request.method} request at {request.path}
                {str(err)}
                """
            )
            return utils.api_error_response("Payload must be a valid JSON")
        return cb_fun(*args, **kw)

    return wrapper


def validate_schema(schema) -> Callable[..., Callable[..., Response]]:
    def decorator(cb_fun: Callable[..., Response]) -> Callable[..., Response]:
        @wraps(cb_fun)
        def wrapper(*args: Any, **kw: Any) -> Response:
            try:
                jsonschema.validate(request.json, schema)
            except jsonschema.ValidationError as err:
                logger.error(
                    f"""Error for {request.method} request at {request.path}
                    {str(err)}
                    """
                )
                return utils.api_error_response(err.message)
            return cb_fun(*args, **kw)

        return wrapper

    return decorator
