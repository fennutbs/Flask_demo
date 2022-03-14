# -*- coding:utf-8 -*-

from app import db, app


class User(db.Model):
    # 指定数据库中关联的表名，如果与类名一致可以不定义
    __tablename__ = "user"
    # 分别指定类中的属性与表中字段的对应关系，如果属性名称和表字段名称一致，可以省略第一个参数
    id = db.Column('id', db.String,  primary_key=True)
    phone = db.Column('phone', db.String)
    pwd = db.Column('pwd', db.String)
    age = db.Column('age', db.Integer)
    email = db.Column('email', db.String)
    address = db.Column('address', db.String)
