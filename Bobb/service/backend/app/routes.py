from flask import Blueprint, jsonify, make_response, request, session, Response, send_file
from app.middlewares import auth_check, validate_json, validate_schema, flag_manager_check
from app.schema import login_or_register_schema, redeem_schema, put_flag_schema
import app.logger as logger
import app.services as services
import app.utils as utils

rest_api = Blueprint("api", __name__, url_prefix="/api")


@rest_api.route("/status", methods=["GET"])
def status() -> Response:
    logger.info(f"Received {request.method} request at {request.path}")
    try:
        res = {"message": "Everything is running smoothly"}
        return make_response(jsonify(res), 200)
    except Exception as err:
        return utils.api_exception(err, request)


@rest_api.route("/me", methods=["GET"])
@auth_check
def me() -> Response:
    logger.info(f"Received {request.method} request at {request.path}")
    try:
        user_id = session.get('user_id')
        res = services.me(user_id)
        return make_response(jsonify(res), 200)
    except Exception as err:
        return utils.api_exception(err, request)


@rest_api.route("/register", methods=["POST"])
@validate_json
@validate_schema(login_or_register_schema)
def register() -> Response:
    logger.info(f"Received {request.method} request at {request.path}")
    try:
        json_data = request.get_json()
        res = services.register(json_data["username"], json_data["password"])
        return make_response(jsonify(res), 200)
    except Exception as err:
        return utils.api_exception(err, request)


@rest_api.route("/login", methods=["POST"])
@validate_json
@validate_schema(login_or_register_schema)
def login() -> Response:
    logger.info(f"Received {request.method} request at {request.path}")
    try:
        json_data = request.get_json()
        res = services.login(json_data["username"], json_data["password"])
        session["user_id"] = res["id"]
        return make_response(jsonify(res), 200)
    except Exception as err:
        return utils.api_exception(err, request)
    

@rest_api.route("/logout", methods=["POST"])
def logout() -> Response:
    logger.info(f"Received {request.method} request at {request.path}")
    try:
        session.pop('user_id')
        res = {'message': 'Logout completed'}
        return make_response(jsonify(res), 200)
    except Exception as err:
        return utils.api_exception(err, request)


@rest_api.route("/redeem", methods=["POST"])
@auth_check
@validate_json
@validate_schema(redeem_schema)
def redeem() -> Response:
    logger.info(f"Received {request.method} request at {request.path}")
    try:
        user_id = session.get('user_id')
        json_data = request.get_json()
        res = services.redeem(user_id, json_data["coupon"])
        return make_response(jsonify(res), 200)
    except Exception as err:
        return utils.api_exception(err, request)


@rest_api.route("/products", methods=["GET"])
@auth_check
def products() -> Response:
    logger.info(f"Received {request.method} request at {request.path}")
    try:
        res = services.products()
        return make_response(jsonify(res), 200)
    except Exception as err:
        return utils.api_exception(err, request)
    
@rest_api.route("/image", methods=["GET"])
def image() -> Response:
    logger.info(f"Received {request.method} request at {request.path}")
    try:
        image_path = request.args.get('path')
        res = services.image(image_path)
        return send_file(res)
    except Exception as err:
        return utils.api_exception(err, request)
    

@rest_api.route("/buy/<int:product_id>", methods=["POST"])
@auth_check
def buy(product_id) -> Response:
    logger.info(f"Received {request.method} request at {request.path}")
    try:
        user_id = session.get('user_id')
        res = services.buy(user_id, product_id)
        return make_response(jsonify(res), 200)
    except Exception as err:
        return utils.api_exception(err, request)

@rest_api.route('flag_manager', methods=['GET'])
@flag_manager_check
def get_flag() -> Response:
    logger.info(f"Received {request.method} request at {request.path}")
    try:
        product_id = request.args.get('id')
        res = services.get_flag(product_id)
        return make_response(jsonify(res), 200)
    except Exception as err:
        return utils.api_exception(err, request)


@rest_api.route('flag_manager', methods=['POST'])
@flag_manager_check
@validate_schema(put_flag_schema)
def put_flag() -> Response:
    logger.info(f"Received {request.method} request at {request.path}")
    try:
        json_data = request.get_json()
        res = services.put_flag(json_data)
        return make_response(jsonify(res), 200)
    except Exception as err:
        return utils.api_exception(err, request)