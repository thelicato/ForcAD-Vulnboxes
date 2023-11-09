from uuid import uuid4
import flask
import app.logger as logger


def get_uuid():
    return uuid4().hex


def api_error_response(msg: str) -> flask.Response:
    response = {"message": msg}
    return flask.make_response(flask.jsonify(response), 400)


def api_exception(err: Exception, request: flask.Request):
    logger.error(
        f"""Error for {request.method} request at {request.path}
        {str(err)}
        """
    )
    return api_error_response(str(err))
