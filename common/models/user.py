from test1 import db1
#用model访问数据库 一个表是一个对象 不用写sql
class User(db1.Model):
    Host = db1.Column(db1.String(80),primary_key = True)
    User = db1.Column(db1.String(200))