# -*- encoding=utf-8 -*-
from . import ModelMixin
from app import db
from datetime import datetime


class Adminlog(db.Model, ModelMixin):
    """
    管理员登录日志
    """
    __tablename__ = "adminlog"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    ip = db.Column(db.String(100))  # 登录IP
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)  # 登录时间

    # 创建外键关系
    admin_id = db.Column(db.Integer, db.ForeignKey('admin.id'))  # 所属管理员ID