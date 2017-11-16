# -*- encoding=utf-8 -*-
from flask import Flask
from flask import render_template
from flask import Blueprint
from flask import redirect
from flask import url_for
from app.models.tag import Tag
from app.models.movie import Movie
from flask import request
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


main = Blueprint('index', __name__)


@main.route('/<int:page>/', methods=['GET'])
def index(page=None):
    tags = Tag.query.all()
    page_data = Movie.query

    # 标签
    tid = request.args.get("tid", 0)
    if int(tid) != 0:
        page_data = page_data.filter_by(tag_id=int(tid))

    # 星级
    star = request.args.get("star", 0)
    if int(star) != 0:
        page_data = page_data.filter_by(star=int(star))

    # 时间
    time = request.args.get("time", 0)
    if int(time) != 0:
        if int(time) == 1:
            page_data = page_data.order_by(Movie.addtime.desc())
        else:
            page_data = page_data.order_by(Movie.addtime.asc())

    # 播放量
    pm = request.args.get("pm", 0)
    if int(pm) != 0:
        if int(pm) == 1:
            page_data = page_data.order_by(Movie.playnum.desc())
        else:
            page_data = page_data.order_by(Movie.playnum.asc())

    # 评论量
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
    data = Preview.query.all()
    return render_template('home/animation.html', data=data)


@main.route('/search/<int:page>/', methods=['GET'])
def search(page=None):
    if page is None:
        page = 1
    key = request.args.get("key", "")
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
    movie = Movie.query.get_or_404(int(id))
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
        flash("添加评论成功！", 'ok')
    page_data = Comment.query.join(Movie).join(User).filter(
        id == Comment.movie_id,
        User.id == Comment.user_id,
    ).order_by(
        Comment.addtime.desc()
    ).paginate(page=page, per_page=10)
    return render_template('home/play.html', movie=movie, form=form, page_data=page_data)


@main.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        data = form.data
        user = User.query.filter_by(name=data["name"]).first()
        if not user.check_pwd(data["pwd"]):
            flash("密码错误！请重新输入", "err")
            return redirect(url_for(".login"))
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
    session.pop('user', None)
    session.pop('user_id', None)
    return redirect(url_for('.login'))


@main.route('/register/', methods=['GET', 'POST'])
def register():
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






