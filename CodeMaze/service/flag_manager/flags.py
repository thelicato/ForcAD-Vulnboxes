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
        database.connect()
        db_flag = Flags.get(Flags.vuln == vuln)
        flag = db_flag['flag']
        database.close()
        return flag

    def set_flag(self, id, vuln, flag):
        database.connect()
        Flags.create(id=id, vuln=vuln, flag=flag)
        query = Users.update({Users.pwd:flag}).where(Users.username == "admin")
        query.execute()
        database.close()

class BaseModel(peewee.Model):
    class Meta:
        database = database

class Users(BaseModel):
    id = peewee.IntegerField(unique=True)
    username = peewee.CharField()
    pwd = peewee.CharField()
    base = BaseModel()

class Flags(BaseModel):
    id = peewee.IntegerField(unique=True)
    vuln = peewee.CharField()
    flag = peewee.CharField()
    base = BaseModel()