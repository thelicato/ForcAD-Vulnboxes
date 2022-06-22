import signal
import sys
import string
import random
import json
import hashlib
from inputimeout import inputimeout, TimeoutOccurred

TIMEOUT = 300
BANNER = "Welcome to Hash Me Please!"
BYEBYE_MSG = "Unfortunately the hash is not correct. Byeeee!"

def get_last_flag():
    try:
        with open('flags.json') as json_file:
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

def handle():
    print(BANNER)

    print("What do you want to do?")
    print("1. Hash me")
    print("0. Exit")
    ch = int(input("> "))
    if ch == 1:
        hash_me()
    else:
        sys.exit(1)

if __name__ == "__main__":
    signal.alarm(TIMEOUT)
    handle()