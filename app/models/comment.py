# -*- encoding=utf-8 -*-
from . import ModelMixin
from app import db
from datetime import datetime


class Comment(db.Model, ModelMixin):
    """
    评论
    """
    __tablename__ = "comment"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    content = db.Column(db.Text)  # 内容
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)  # 添加时间

    # 引用外键
    movie_id = db.Column(db.Integer, db.ForeignKey("movie.id"))  # 所属电影
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))  # 所属用户