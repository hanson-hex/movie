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

    # 定义外键关系
    userlogs = db.relationship('Userlog', backref="user")  # 会员日志外键关系
    comments = db.relationship('Comment', backref="user")  # 会员评论外键关系
    moviecols = db.relationship("Moviecol", backref="user")  # 电影收藏外键关联

    def check_pwd(self, pwd):
        return check_password_hash(self.pwd, pwd)


# 电影
class Movie(db.Model):
    __tablename__ = "movie"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    title = db.Column(db.String(255), unique=True)  # 电影标题
    url = db.Column(db.String(255), unique=True)  # 网址
    info = db.Column(db.Text)  # 信息
    logo = db.Column(db.String(255), unique=True)  # 封面
    star = db.Column(db.SmallInteger)  # 星级
    playnum = db.Column(db.BigInteger)  # 播放量
    commentnum = db.Column(db.BigInteger)  # 评论量
    tag_id = db.Column(db.Integer, db.ForeignKey("tag.id"))  # 标签外键
    area = db.Column(db.String(255))  # 地区
    release_time = db.Column(db.Date)  # 放映时间
    length = db.Column(db.String(100))  # 电影长度
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)  # 放映时间
    comments = db.relationship("Comment", backref="movie")  # 评论外键关联
    moviecols = db.relationship("Moviecol", backref="movie")  # 收藏外键关联




    def __repr__(self):
        return "<Auth %r>" % self.name


# 角色
class Role(db.Model):
    __tablename__ = "role"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    name = db.Column(db.String(100), unique=True)  # 名称
    auths = db.Column(db.String(600))  # 权限
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)  # 添加时间
    admins = db.relationship("Admin", backref="role")  # 管理员外键关联

    def __repr__(self):
        return "<Role %r>" % self.name


# 管理员
class Admin(db.Model):
    __tablename__ = "admin"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    name = db.Column(db.String(100), unique=True)  # 名称
    pwd = db.Column(db.String(100))  # 管理员密码
    is_super = db.Column(db.SmallInteger)  # 是否为超级管理员 0为超级管理员
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))  # 角色的外键
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)  # 添加时间
    adminlogs = db.relationship("Adminlog", backref="admin")  # 管理员日志外键关联
    oplogs = db.relationship("Oplog", backref="admin")  # 管理员操作日志外键关联

    def __repr__(self):
        return "<Admin %r>" % self.name

    def check_pwd(self, pwd):
        from werkzeug.security import check_password_hash
        return check_password_hash(self.pwd, pwd)



# 管理员登录日志
class Adminlog(db.Model):
    __tablename__ = "adminlog"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    admin_id = db.Column(db.Integer, db.ForeignKey('admin.id'))  # 所属管理员ID
    ip = db.Column(db.String(100))  # 登录IP
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)  # 登录时间

    def __repr__(self):
        return "<Adminlog %r>" % self.id


# 操作日志
class Oplog(db.Model):
    __tablename__ = "oplog"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    admin_id = db.Column(db.Integer, db.ForeignKey('admin.id'))  # 所属管理员ID
    reason = db.Column(db.String(600))  # 操作原因
    ip = db.Column(db.String(100))  # 操作IP
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)  # 登录时间
