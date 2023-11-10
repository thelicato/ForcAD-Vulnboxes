import os
import requests
import yaml
from checklib import *

PORT = 5002

class CheckMachine:

    def __init__(self, checker):
        self.checker = checker
        self.token = ''
        dir_path = os.path.dirname(os.path.realpath(__file__))
        with open(f"{dir_path}/config.yml", "r") as stream:
            try:
                config = yaml.safe_load(stream)
                self.token = config[checker.host]
            except yaml.YAMLError as exc:
                print(exc)

    def ping(self):
        r_index = requests.get(
            'http://hashmeplease_bridge:5000/bridge/status',
            params={
                'host': self.checker.host,
                'port': PORT,
            },
            timeout=2
        )
        self.checker.check_response(r_index, 'Check failed')

    def put_flag(self, flag, vuln):
        new_id = rnd_string(10)
        r = requests.get(
            'http://hashmeplease_bridge:5000/bridge/put_flag',
            params={
                'host': self.checker.host,
                'port': PORT,
                'token': self.token,
                'id': new_id,
                'vuln': vuln,
                'flag': flag,
            },
            timeout=2,
        )
        self.checker.check_response(r, 'Could not put flag')

        return new_id

    def get_flag(self, flag_id, vuln):
        r = requests.get(
            'http://hashmeplease_bridge:5000/bridge/get_flag',
            params={
                'host': self.checker.host,
                'port': PORT,
                'token': self.token,
                'id': flag_id,
                'vuln': vuln,
            },
            timeout=2,
        )
        self.checker.check_response(r, 'Could not get flag')
        data = self.checker.get_json(r, 'Invalid response from bridge')
        self.checker.assert_in(
            'flag', data,
            'Could not get flag',
            status=Status.CORRUPT,
        )
        return data['flag']
