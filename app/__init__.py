# -*- coding:utf-8 -*-

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql
pymysql.install_as_MySQLdb()


class Config(object):
    SQLALCHEMY_DATABASE_URI = 'mysql://root:123456@localhost:3306/stock'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)


from . import models, views