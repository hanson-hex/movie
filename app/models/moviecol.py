# -*- encoding=utf-8 -*-
from . import ModelMixin
from app import db
from datetime import datetime


class Moviecol(db.Model, ModelMixin):
    """
    电影收藏
    """
    __tablename__ = "moviecol"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)  # 添加时间

    # 创建外键
    movie_id = db.Column(db.Integer, db.ForeignKey("movie.id"))  # 所属电影
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))  # 所属用户


    def __init__(self, form):
        self.movie_id = int(form.get('movie_id', -1))
        self.user_id = int(form.get('user_id', -1))