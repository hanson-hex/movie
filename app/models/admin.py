# -*- encoding=utf-8 -*-
from . import ModelMixin
from app import db
from datetime import datetime
from werkzeug.security import check_password_hash


class Admin(db.Model):
    """
    管理员
    """
    __tablename__ = "admin"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    name = db.Column(db.String(100), unique=True)  # 名称
    pwd = db.Column(db.String(100))  # 管理员密码
    is_super = db.Column(db.SmallInteger)  # 是否为超级管理员 0为超级管理员
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)  # 添加时间

    # 创建外键
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))  # 角色的外键

    # 引用外键关系
    adminlogs = db.relationship("Adminlog", backref="admin")  # 管理员日志外键关联
    oplogs = db.relationship("Oplog", backref="admin")  # 管理员操作日志外键关联

    def check_pwd(self, pwd):
        return check_password_hash(self.pwd, pwd)