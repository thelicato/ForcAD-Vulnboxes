import os
import json
import requests
import yaml
from checklib import *

PORT = 5004

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
        r = requests.get(f'http://{self.checker.host}:{PORT}', timeout=2)
        self.checker.check_response(r, 'Check failed')

    def put_flag(self, flag, vuln):
        new_id = rnd_string(10)
        # Send dummy flag
        requests.post(
            f'http://{self.checker.host}:{PORT}/api/flag_manager',
            headers={
                'Authorization': f"Bearer {self.token}",
                'Content-type': 'application/json'
            },
            json={
                'hash': new_id,
                'value': flag
            },
            timeout=2,
        )
        self.checker.check_response(r, 'Could not put flag')

        return new_id

    def get_flag(self, flag_id, vuln):
        r = requests.get(
            f'http://{self.checker.host}:{PORT}/api/flag_manager',
            headers={
                'Authorization': f"Bearer {self.token}",
                'Content-type': 'application/json'
            },
            params={
                # Switch id and vuln for consistency
                'hash': flag_id,
            },
            timeout=2,
        )
        self.checker.check_response(r, 'Could not get flag')
        data = self.checker.get_json(r, 'Invalid response from /api/flag_manager')
        self.checker.assert_in(
            'flag', data['flag'],
            'Could not get flag',
            status=Status.CORRUPT,
        )
        return data['flag']
