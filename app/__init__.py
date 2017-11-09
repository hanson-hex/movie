# -*- encoding=utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql
import os

app = Flask(__name__)
# 将配置文件引入
app.config.from_pyfile('app.conf')


db = SQLAlchemy(app)

from app.admin_routes import index