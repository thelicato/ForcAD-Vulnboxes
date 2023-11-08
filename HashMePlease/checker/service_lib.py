import os
import requests
import yaml
from checklib import *
from pwn import *

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
        try:
            conn = remote(self.checker.host, port)
            conn.recvuntil(b'>')
            conn.close()
        except:
            self.checker.cquit(status.Status.DOWN, "Unable to connect", "Unable to connect")

    def put_flag(self, flag, vuln):
        new_id = rnd_string(10)
        try:
            conn = remote(self.checker.host, port)
            conn.recvuntil(b'>')
            conn.sendline(b'2')
            conn.recvuntil(b'>')
            conn.sendline(b'2')
            conn.recvuntil(b'Token:')
            conn.sendline(self.token.encode('utf-8'))
            conn.recvuntil(b'ID:')
            conn.sendline(new_id.encode('utf-8'))
            conn.recvuntil(b'Vuln:')
            conn.sendline(vuln.encode('utf-8'))
            conn.recvuntil(b'Flag:')
            conn.sendline(flag.encode('utf-8'))
            received_text = conn.recvline().strip()
            if not "Flag correctly set" in received_text:  
                raise Exception('Unable to set flag')
            return new_id
        except:
            self.checker.cquit(status.Status.CORRUPT, "Unable to set flag", "Unable to set flag")
        

    def get_flag(self, flag_id, vuln):
        try:
            conn = remote(self.checker.host, port)
            conn.recvuntil(b'>')
            conn.sendline(b'2')
            conn.recvuntil(b'>')
            conn.sendline(b'1')
            conn.recvuntil(b'Token:')
            conn.sendline(self.token.encode('utf-8'))
            conn.recvuntil(b'ID:')
            conn.sendline(flag_id.encode('utf-8'))
            conn.recvuntil(b'Vuln:')
            conn.sendline(vuln.encode('utf-8'))
            received_text = conn.recvline().strip()
            self.checker.assert_in(
                'flag', data,
                'Could not get flag',
                status=Status.CORRUPT,
            )
            return data
        except:
            self.checker.cquit(status.Status.CORRUPT, "Unable to get flag", "Unable to get flag")