# -*- encoding=utf-8 -*-
from . import ModelMixin
from app import db
from datetime import datetime


#
class Oplog(db.Model, ModelMixin):
    """
    操作日志
    """
    __tablename__ = "oplog"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    reason = db.Column(db.String(600))  # 操作原因
    ip = db.Column(db.String(100))  # 操作IP
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)  # 登录时间

    # 创建外键
    admin_id = db.Column(db.Integer, db.ForeignKey('admin.id'))  # 所属管理员ID