# -*- encoding=utf-8 -*-
from . import ModelMixin
from app import db
from datetime import datetime


class Userlog(db.Model, ModelMixin):
    """
    会员登录日志
    """
    __tablename__ = "userlog"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    ip = db.Column(db.String(100))  # 登录IP
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)  # 登录时间

    # 创建外键
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  # 所属会员ID