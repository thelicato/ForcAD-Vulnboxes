import flags
from flask import Blueprint, jsonify, make_response, request
from middlewares import flag_manager_check

rest_api = Blueprint('api', __name__)

@rest_api.route('/ping/', methods = ['GET'])
@flag_manager_check
def ping():
    return make_response("I am alive!")

@rest_api.route('/get/', methods = ['GET'])
@flag_manager_check
def get_flag():
    try:
        args = request.args
        id = args['id']
        vuln = args['vuln']
        flag = flags.Singleton().get_flag(id, vuln)
        return make_response(jsonify({'flag': flag}))
    except Exception as e:
        return make_response(str(e))

@rest_api.route('/put/', methods = ['POST'])
@flag_manager_check
def set_flag():
    try:
        body = request.get_json()
        id = body['id']
        vuln = body['vuln']
        flag = body['flag']
        flags.Singleton().set_flag(id, vuln, flag)
        return make_response('Flag correctly set')
    except Exception as e:
        return make_response(str(e))