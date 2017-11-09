# -*- encoding=utf-8 -*-
from . import ModelMixin
from app import db
from datetime import datetime


class Tag(db.Model, ModelMixin):
    """
    标签
    """
    __tablename__ = "tag"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    name = db.Column(db.String(100), unique=True)  # 标题
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)  # 添加时间

    # 定义外键关系
    movies = db.relationship("Movie", backref="tag")  # 电影的外键关联