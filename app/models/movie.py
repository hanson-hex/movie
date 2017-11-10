# -*- encoding=utf-8 -*-
from . import ModelMixin
from app import db
from datetime import datetime


class Movie(db.Model, ModelMixin):
    """
    电影
    """
    __tablename__ = "movie"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    title = db.Column(db.String(255), unique=True)  # 电影标题
    url = db.Column(db.String(255), unique=True)  # 网址
    info = db.Column(db.Text)  # 信息
    logo = db.Column(db.String(255), unique=True)  # 封面
    star = db.Column(db.SmallInteger)  # 星级
    playnum = db.Column(db.BigInteger)  # 播放量
    commentnum = db.Column(db.BigInteger)  # 评论量
    area = db.Column(db.String(255))  # 地区
    release_time = db.Column(db.Date)  # 放映时间
    length = db.Column(db.String(100))  # 电影长度
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)  # 放映时间


    # 创建外键
    tag_id = db.Column(db.Integer, db.ForeignKey("tag.id"))  # 标签外键

    # 引用外键关系
    comments = db.relationship("Comment", backref="movie")  # 评论外键关联
    moviecols = db.relationship("Moviecol", backref="movie")  # 收藏外键关联