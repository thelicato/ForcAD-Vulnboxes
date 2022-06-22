import os
import peewee
import json

dbschema = os.getenv('DBSCHEMA', default=None)
dbuser = os.getenv('DBUSER', default=None)
dbpwd = os.getenv('DBPASS', default=None)
dbhost = os.getenv('DBHOST', default=None)

database = peewee.MySQLDatabase(dbschema, user=dbuser, password=dbpwd, host=dbhost, port=3306)

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
        User.update(pwd=flag).where(User.username == "admin")

class BaseModel(peewee.Model):
    class Meta:
        database = database

class User(BaseModel):
    id = peewee.IntegerField(unique=True)
    username = peewee.CharField()
    pwd = peewee.CharField()
    base = BaseModel()