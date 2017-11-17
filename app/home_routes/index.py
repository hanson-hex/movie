# -*- encoding=utf-8 -*-
from flask import Flask
from flask import render_template
from flask import Blueprint
from flask import redirect
from flask import url_for
from app.models.tag import Tag
from app.models.movie import Movie
from flask import request
from flask import Response
from app.home_routes.forms import LoginForm
from app.home_routes.forms import UserForm
from flask import session
from app.models.userlog import Userlog
from app.models.user import User
from flask import flash
from app.models.userlog import Userlog
from app.utils import log
from app.home_routes.forms import CommentForm
from app.models.preview import Preview
from app.models.comment import Comment
import datetime
import os
from app import rd
import uuid
import json


main = Blueprint('index', __name__)


@main.route('/<int:page>/', methods=['GET'])
def index(page=None):
    """
    首页
    """
    tags = Tag.query.all()
    page_data = Movie.query

    # 标签排序
    tid = request.args.get("tid", 0)
    if int(tid) != 0:
        page_data = page_data.filter_by(tag_id=int(tid))

    # 星级排序
    star = request.args.get("star", 0)
    if int(star) != 0:
        page_data = page_data.filter_by(star=int(star))

    # 时间排序
    time = request.args.get("time", 0)
    if int(time) != 0:
        if int(time) == 1:
            page_data = page_data.order_by(Movie.addtime.desc())
        else:
            page_data = page_data.order_by(Movie.addtime.asc())

    # 播放量排序
    pm = request.args.get("pm", 0)
    if int(pm) != 0:
        if int(pm) == 1:
            page_data = page_data.order_by(Movie.playnum.desc())
        else:
            page_data = page_data.order_by(Movie.playnum.asc())

    # 评论量排序
    cm = request.args.get("cm", 0)
    if int(cm) != 0:
        if int(cm) == 1:
            page_data = page_data.order_by(Movie.commentnum.desc())
        else:
            page_data = page_data.order_by(Movie.commentnum.asc())

    if page is None:
        page = 1
    data = dict(
        tid=tid,
        star=star,
        time=time,
        pm=pm,
        cm=cm,
    )
    page_data = page_data.paginate(page=page, per_page=12)
    return render_template('home/index.html ', page_data=page_data, data=data, tags=tags)


@main.route('/animation/')
def animation():
    """
    预告动画制作
    """
    data = Preview.query.all()
    return render_template('home/animation.html', data=data)


@main.route('/search/<int:page>/', methods=['GET'])
def search(page=None):
    """
    搜索页面
    """
    if page is None:
        page = 1
    key = request.args.get("key", "")
    # 关键词
    movie_count = Movie.query.filter(
        Movie.title.ilike('%' + key + '%')
    ).count()
    page_data = Movie.query.filter(
        Movie.title.ilike('%' + key + '%')
    ).order_by(
        Movie.addtime.desc()
    ).paginate(page=page, per_page=12)
    return render_template('home/search.html', page_data=page_data, key=key, movie_count=movie_count)


@main.route('/play/<int:id>/<int:page>/', methods=['GET','POST'])
def play(id=None, page=None):
    """
     播放界面
    """
    movie = Movie.query.get_or_404(int(id))
    movie.playnum = movie.playnum + 1
    form = CommentForm()
    if page is None:
        page = 1
    if "user" in session and form.validate_on_submit():
        data = form.data
        form = dict(
            content=data["content"],
            movie_id=int(id),
            user_id=session['user_id']
        )
        comment = Comment(form)
        comment.save()
        movie.commentnum = movie.commentnum + 1
        movie.save()
        flash("添加评论成功！", 'ok')
        return redirect(url_for('index.play', id=movie.id, page=1))
    movie.save()
    page_data = Comment.query.join(Movie).join(User).filter(
        id == Comment.movie_id,
        User.id == Comment.user_id,
    ).order_by(
        Comment.addtime.desc()
    ).paginate(page=page, per_page=10)
    return render_template('home/play.html', movie=movie, form=form, page_data=page_data)


@main.route('/video/<int:id>/<int:page>/', methods=['GET','POST'])
def video(id=None, page=None):
    """
    弹幕播放尝试
    """
    movie = Movie.query.get_or_404(int(id))
    movie.playnum = movie.playnum + 1
    form = CommentForm()
    if page is None:
        page = 1
    if "user" in session and form.validate_on_submit():
        data = form.data
        form = dict(
            content=data["content"],
            movie_id=int(id),
            user_id=session['user_id']
        )
        comment = Comment(form)
        comment.save()
        movie.commentnum = movie.commentnum + 1
        movie.save()
        flash("添加评论成功！", 'ok')
        return redirect(url_for('index.video', id=movie.id, page=1))
    movie.save()
    page_data = Comment.query.join(Movie).join(User).filter(
        id == Comment.movie_id,
        User.id == Comment.user_id,
    ).order_by(
        Comment.addtime.desc()
    ).paginate(page=page, per_page=10)
    return render_template('home/video.html', movie=movie, form=form, page_data=page_data)


@main.route("/tm/", methods=["GET", "POST"])
def tm():
    """
    弹幕
    """

    # 获取弹幕消息
    if request.method == "GET":
            id = request.args.get('id')
            key = "movie" + str(id)
            log('rd.llen(key)', rd.llen(key))
            if rd.llen(key):
                msgs = rd.lrange(key, 0, 2999)
                log('msgs', rd.lrange(key, 0, 2999))
                res = {
                "code": 1,
                "danmaku": [json.loads(v.decode('utf-8')) for v in msgs]
                }
            else:
                res = {
                "code": 1,
                "danmaku": []
                }
            resp = json.dumps(res)
    # 提交新弹幕
    if request.method == "POST":
        d = request.get_data().decode('utf-8')
        log('d', d)
        data = json.loads(d)
        msg = {
            "__v": 0,
            "author": data["author"],
            "time": data["time"],
            "text": data["text"],
            "color": data["color"],
            "type": data['type'],
            "ip": request.remote_addr,
            "_id": datetime.datetime.now().strftime("%Y%m%d%H%M%S") +
            uuid.uuid4().hex,
        "player": [
            data["player"]
            ]
        }
        res = {
            "code": 1,
            "data": msg
        }
        resp = json.dumps(res)
        rd.lpush("movie" + str(data["player"]), json.dumps(msg))
    return Response(resp, mimetype='application/json')


@main.route('/login/', methods=['GET', 'POST'])
def login():
    """
    会员登录页面
    """
    form = LoginForm()
    if form.validate_on_submit():
        data = form.data
        user = User.query.filter_by(name=data["name"]).first()
        # 密码错误
        if not user.check_pwd(data["pwd"]):
            flash("密码错误！请重新输入", "err")
            return redirect(url_for(".login"))
        # 保存用户状态
        session["user"] = data["name"]
        session["user_id"] = user.id
        form = dict(
            user_id=session["user_id"],
            ip=request.remote_addr,
        )
        userlog = Userlog(form)
        userlog.save()
        return redirect(url_for("user.user"))
    return render_template('home/login.html', form=form)


@main.route('/logout/')
def logout():
    """
    退出登录
    """
    session.pop('user', None)
    session.pop('user_id', None)
    return redirect(url_for('.login'))


@main.route('/register/', methods=['GET', 'POST'])
def register():
    """
    会员注册
    """
    form = UserForm()
    log('进入登录页面')
    if form.validate_on_submit():
        data = form.data
        user = User(data)
        log('user', user)
        user.save()
        flash("注册成功！", "ok")
        return redirect(url_for(".register"))
    return render_template('home/register.html', form=form)






