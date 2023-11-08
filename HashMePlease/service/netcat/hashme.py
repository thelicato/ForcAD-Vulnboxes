import os
import signal
import sys
import string
import random
import json
import hashlib
from pathlib import Path
from inputimeout import inputimeout, TimeoutOccurred

DATA_FOLDER = "/data"
TIMEOUT = 300
BANNER = "Welcome to Hash Me Please!"
BYEBYE_MSG = "Unfortunately the hash is not correct. Byeeee!"

def create_file_if_missing():
    file = Path(f"{DATA_FOLDER}/flags.json")
    if not file.is_file():
        file.touch()

def load_flags_file():
    try:
        with open(f"{DATA_FOLDER}/flags.json", 'r') as file:
            data = json.load(file)
            return data
    except json.JSONDecodeError:
        return []
    except FileNotFoundError:
        return []
    except Exception as e:
        return []

def get_last_flag():
    try:
        with open(f"{DATA_FOLDER}/flags.json") as json_file:
            data = json.load(json_file)
            return data[-1]['flag']
    except:
        print("An error occured, it's not your fault!")

def hash_me():
    random_value = ''.join(random.sample(string.ascii_lowercase,15))
    correct_hash = hashlib.sha512(random_value.encode()).hexdigest() 
    print(f"If you hash me I'll give you a gift: {random_value}")
    try:
        user_hash = inputimeout(prompt='>>', timeout=5)
        if user_hash == correct_hash:
            print(f"Here is your flag: {get_last_flag()}")
        else:
            print(BYEBYE_MSG)
    except TimeoutOccurred:
        print(BYEBYE_MSG)

def get_flag():
    token = input("Token: ")
    if token != os.environ['FLAG_MANAGER_SECRET']:
        print("Wrong token")
        sys.exit(1)
    flag_id = input("ID: ")
    vuln = input("Vuln: ")
    flags = load_flags_file()
    is_correct_flag = lambda f: f['id'] == flag_id and f['vuln'] == vuln
    flag = next(filter(is_correct_flag, flags), None)['flag']
    print(flag)

def put_flag():
    token = input("Token: ")
    if token != os.environ['FLAG_MANAGER_SECRET']:
        print("Wrong token")
        sys.exit(1)
    flag_id = input("ID: ")
    vuln = input("Vuln: ")
    flag = input("Value: ")

    current_flags = load_flags_file()
    with open(f"{DATA_FOLDER}/flags.json", 'w') as outfile:
        new_flag = {'id': flag_id, 'vuln': vuln, 'flag': flag}
        current_flags.append(new_flag)
        json.dump(current_flags, outfile, sort_keys=True, indent=4, separators=(',', ': '))
    
    print("Flag correctly set!")

def manage():
    print("1. Get flag")
    print("2. Put flag")
    print("0. Exit")
    ch = int(input("> "))
    if ch == 1:
        get_flag()
    if ch == 2:
        put_flag()
    else:
        sys.exit(1)

def handle():
    print(BANNER)
    create_file_if_missing()

    print("What do you want to do?")
    print("1. Hash me")
    print("2. Manage")
    print("0. Exit")
    ch = int(input("> "))
    if ch == 1:
        signal.alarm(TIMEOUT)
        hash_me()
    if ch == 2:
        manage()
    else:
        sys.exit(1)

if __name__ == "__main__":
    handle()