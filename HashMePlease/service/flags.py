import datetime
import json

class Singleton():
    flags = []

    """Implement it as a Singleton"""
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance

    def get_flag(self, id, vuln):
        is_correct_flag = lambda f: f['id'] == id and f['vuln'] == vuln
        flag = next(filter(is_correct_flag, self.flags), None)['flag']
        return flag

    def set_flag(self, id, vuln, flag):
        new_flag = {'id': id, 'vuln': vuln, 'flag': flag}
        self.flags.append(new_flag)
        with open('flags.json', 'w') as outfile:
            json.dump(self.flags, outfile, sort_keys=True, indent=4, separators=(',', ': '))