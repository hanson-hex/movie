# -*- encoding=utf-8 -*-
from . import ModelMixin
from app import db
from datetime import datetime


class Preview(db.Model, ModelMixin):
    """
    上映预告
    """
    __tablename__ = "preview"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    title = db.Column(db.String(255), unique=True)  # 电影标题
    logo = db.Column(db.String(255), unique=True)  # 预告封面
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)  # 添加时间