# -*- encoding=utf-8 -*-
from . import ModelMixin
from app import db
from datetime import datetime
from werkzeug.security import check_password_hash

class User(db.Model, ModelMixin):
    """
    会员
    """
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)  # 编号
    name = db.Column(db.String(100), unique=True)  # 名称
    pwd = db.Column(db.String(100))  # 密码
    email = db.Column(db.String(100), unique=True)  # 邮箱
    phone = db.Column(db.String(11), unique=True)  # 电话
    info = db.Column(db.Text)  # 个性简介
    face = db.Column(db.String(255), unique=True)  # 头像
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)  # 注册时间
    uuid = db.Column(db.String(255), unique=True)  # 唯一标识符

    # 引用外键关系
    userlogs = db.relationship('Userlog', backref="user")  # 会员日志外键关系
    comments = db.relationship('Comment', backref="user")  # 会员评论外键关系
    moviecols = db.relationship("Moviecol", backref="user")  # 电影收藏外键关联

    def check_pwd(self, pwd):
        return check_password_hash(self.pwd, pwd)



