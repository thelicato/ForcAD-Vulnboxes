import peewee

database = peewee.SqliteDatabase('db.sqlite')  # Defer initialization


class BaseModel(peewee.Model):
    class Meta:
        database = database


class User(BaseModel):
    id = peewee.CharField(primary_key=True)
    username = peewee.CharField(unique=True)
    password = peewee.CharField()
    credit = peewee.IntegerField(default=0)
    base = BaseModel()


class Coupon(BaseModel):
    id = peewee.CharField(primary_key=True)
    value = peewee.IntegerField(default=10)
    used = peewee.BooleanField(default=False)
    user = peewee.ForeignKeyField(User, backref='coupons')
    base = BaseModel()


class Product(BaseModel):
    id = peewee.CharField(primary_key=True)
    name = peewee.CharField()
    description = peewee.CharField()
    value = peewee.CharField()
    price = peewee.IntegerField()
    image = peewee.CharField()
    hash = peewee.CharField()
    ts = peewee.FloatField()
    base = BaseModel()
