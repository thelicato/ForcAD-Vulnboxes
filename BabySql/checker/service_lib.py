import requests
import yaml
from checklib import *

PORT = 5003

class CheckMachine:

    def __init__(self, checker):
        self.checker = checker
        self.token = ''
        with open("config.yml", "r") as stream:
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
        r = requests.post(
            f'http://{self.checker.host}:{PORT}/flag_manager.php',
            headers={
                'Authorization': f"Bearer {self.token}"
            },
            json={
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
            f'http://{self.checker.host}:{PORT}/flag_manager.php',
            headers={
                'Authorization': f"Bearer {self.token}"
            },
            params={
                'id': flag_id,
                'vuln': vuln,
            },
            timeout=2,
        )
        self.checker.check_response(r, 'Could not get flag')
        data = self.checker.get_json(r, 'Invalid response from /flag_manager.php')
        self.checker.assert_in(
            'flag', data,
            'Could not get flag',
            status=Status.CORRUPT,
        )
        return data['flag']
