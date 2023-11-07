import flags
from flask import Blueprint, jsonify, make_response, request

rest_api = Blueprint('api', __name__)

@rest_api.route('/ping/', methods = ['GET'])
def ping():
    return make_response("I am alive!")

@rest_api.route('/get/', methods = ['GET'])
def get_flag():
    try:
        args = request.args
        id = args['id']
        vuln = args['vuln']
        print(f"Looking for flag with id '{id}' and vuln '{vuln}'")
        flag = flags.Singleton().get_flag(id, vuln)
        print(f"Flag found: {flag}")
        return make_response(jsonify({'flag': flag}))
    except Exception as e:
        return make_response(str(e))

@rest_api.route('/put/', methods = ['POST'])
def set_flag():
    try:
        body = request.get_json()
        id = body['id']
        vuln = body['vuln']
        flag = body['flag']
        print(f"Setting flag with id '{id}' - vuln '{vuln}' - value '{flag}'")
        flags.Singleton().set_flag(id, vuln, flag)
        return make_response('Flag correctly set')
    except Exception as e:
        return make_response(str(e))