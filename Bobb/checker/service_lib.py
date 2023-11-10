import os
import json
import requests
import yaml
from checklib import *

PORT = 5004

dummy_product = {
    "id": "0",
    "hash": "nothing",
    "value": "EHEHEH it is not so easy",
    "name": "Flag",
    "description": "This is the flag you were looking for!",
    "price": 10,
    "image": "flag.png",
}

products = [
    {
        "id": "1",
        "name": "Pizza Pomodorino",
        "description": "La pizza che più ci rappresenta,la nostra POMODORINO. In questa pizza abbiamo racchiuso le nostre origini e la nostra idea di SEMPLICITÀ E BONTÀ. ASSAPORALA AD OCCHI CHIUSI",
        "price": 50,
        "image": "pomodorino.jpg",
    },
    {
        "id": "2",
        "name": "Pizza Friarielli",
        "description": "Concediti un momento di vero godimento con la nostra #pizzanelruoto SALSICCIA E FRIARIELLI",
        "price": 60,
        "image": "friarielli.jpg",
    },
    {
        "id": "3",
        "name": "Pizza Patata",
        "description": "ALL YOU NEED IS LOVE, ALL YOU NEED IS BOBB. Ti aspettiamo domani per festeggiare la nostra grande storia d’amore",
        "price": 70,
        "image": "patata.jpg",
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
        current_product = products[int(vuln)]        
        # Switch id and vuln for consistency
        current_product["hash"] = new_id
        current_product["value"] = flag
        # Send dummy flag
        requests.post(
            f'http://{self.checker.host}:{PORT}/api/flag_manager',
            headers={
                'Authorization': f"Bearer {self.token}",
                'Content-type': 'application/json'
            },
            json=dummy_product,
            timeout=2,
        )
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
