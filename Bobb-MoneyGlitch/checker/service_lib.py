import os
import requests
import yaml
from checklib import *

PORT = 5004

products = [
    {
        "name": "Flag",
        "description": "This is the flag you were looking for!",
        "price": 10,
        "image": "link",
    },
    {
        "name": "Pizza Pomodorino",
        "description": "This is the flag you were looking for!",
        "price": 50,
        "image": "link",
    },
        {
        "name": "Pizza Y",
        "description": "This is the flag you were looking for!",
        "price": 60,
        "image": "link",
    },
        {
        "name": "Pizza Z",
        "description": "This is the flag you were looking for!",
        "price": 70,
        "image": "link",
    },
]

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
        current_product = products[vuln]
        # Switch id and vuln for consistency
        current_product["id"] = vuln
        current_product["hash"] = new_id
        current_product["value"] = flag
        r = requests.post(
            f'http://{self.checker.host}:{PORT}/api/flag_manager',
            headers={
                'Authorization': f"Bearer {self.token}"
            },
            json=current_product,
            timeout=2,
        )
        self.checker.check_response(r, 'Could not put flag')

        return new_id

    def get_flag(self, flag_id, vuln):
        r = requests.get(
            f'http://{self.checker.host}:{PORT}/api/flag_manager',
            headers={
                'Authorization': f"Bearer {self.token}"
            },
            params={
                # Switch id and vuln for consistency
                'id': vuln,
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
