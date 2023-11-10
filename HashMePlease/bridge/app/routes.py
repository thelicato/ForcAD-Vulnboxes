from flask import Blueprint, jsonify, make_response, request, session, Response, send_file
import app.logger as logger
import app.netcat as netcat
import app.utils as utils

rest_api = Blueprint("api", __name__, url_prefix="/bridge")

@rest_api.route("/status", methods=["GET"])
def status() -> Response:
    logger.info(f"Received {request.method} request at {request.path}")
    try:
        host = request.args.get('host')
        port = request.args.get('port')
        
        netcat.status(host, port)
        res = {"message": "Everything is running smoothly"}
        return make_response(jsonify(res), 200)
    except Exception as err:
        return utils.api_exception(err, request)


@rest_api.route('get_flag', methods=['GET'])
def get_flag() -> Response:
    logger.info(f"Received {request.method} request at {request.path}")
    try:
        host = request.args.get('host')
        port = request.args.get('port')
        token = request.args.get('token')
        flag_id = request.args.get('flag_id')
        vuln = request.args.get('vuln')
        
        res = netcat.get_flag(host, port, token, flag_id, vuln)
        return make_response(jsonify(res), 200)
    except Exception as err:
        return utils.api_exception(err, request)


@rest_api.route('put_flag', methods=['GET'])
def put_flag() -> Response:
    logger.info(f"Received {request.method} request at {request.path}")
    try:
        host = request.args.get('host')
        port = request.args.get('port')
        token = request.args.get('token')
        flag_id = request.args.get('flag_id')
        flag = request.args.get('flag')
        vuln = request.args.get('vuln')
        
        res = netcat.put_flag(host, port, token, flag_id, flag, vuln)
        return make_response(jsonify(res), 200)
    except Exception as err:
        return utils.api_exception(err, request)