# -*- encoding=utf-8 -*-
from . import ModelMixin
from app import db
from datetime import datetime


class Auth(db.Model, ModelMixin):
    """
    权限
    """
    __tablename__ = "auth"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    name = db.Column(db.String(100), unique=True)  # 名称
    url = db.Column(db.String(255), unique=True)  # 地址
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)  # 添加时间

