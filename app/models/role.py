# -*- encoding=utf-8 -*-
from . import ModelMixin
from app import db
from datetime import datetime


class Role(db.Model, ModelMixin):
    """
    角色
   """
    __tablename__ = "role"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    name = db.Column(db.String(100), unique=True)  # 名称
    auths = db.Column(db.String(600))  # 权限
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)  # 添加时间

    # 创建外键
    admins = db.relationship("Admin", backref="role")  # 管理员外键关联

    def __init__(self, form):
        self.name = form.get('name', '')
        self.auths = form.get('auths', '')
