# -*- encoding=utf-8 -*-
from flask import Flask
from flask import render_template
from flask import Blueprint
from flask import redirect
from flask import url_for
import os
from werkzeug.utils import  secure_filename
from werkzeug.security import generate_password_hash
from flask import flash
from flask import request
from app.home_routes.forms import UserdetailForm
from flask import session
from app.models.user import User
from app import app
from app.home_routes.forms import PwdForm
from app.models.comment import Comment
from app.models.userlog import Userlog
from app.models.moviecol import Moviecol
from app.models.movie import Movie
from datetime import datetime
from . import user_login_req
import uuid

main = Blueprint('user', __name__)

def change_filename(filename):
    fileinfo = os.path.splitext(filename)
    newname = datetime.now().strftime("%Y%m%d%H%M%S") + str(uuid.uuid4().hex) + fileinfo[-1]
    return newname


@main.route('/')
@user_login_req
def user():
    return redirect(url_for('.profile'))


@main.route('/profile/', methods=['GET', 'POST'])
@user_login_req
def profile():
    form = UserdetailForm()
    user = User.query.filter_by(name=session["user"]).first()
    form.face.validators = []
    if request.method == "GET":
        form.name.data = user.name
        form.email.data = user.email
        form.phone.data = user.phone
        form.info.data = user.info
    if form.validate_on_submit():
        data = form.data
        file_face = secure_filename(form.face.data.filename)
        if not os.path.exists(app.config["FC_DIR"]):
            os.makedirs(app.config["FC_DIR"])
            os.chmod(app.config["FC_DIR"], "rw")
        user.face = change_filename(file_face)
        form.face.data.save(app.config["FC_DIR"] + user.face)
        name_count = User.query.filter_by(name=data["name"]).count()
        if name_count == 1 and data["name"] != user.name:
            flash("昵称已经存在！", "err")
            return redirect(url_for("home.user", form=form, user=user))
        email_count = User.query.filter_by(email=data["email"]).count()
        if email_count == 1 and data["email"] != user.email:
            flash("邮箱已经存在！", "err")
            return redirect(url_for("home.user", form=form, user=user))
        phone_count = User.query.filter_by(phone=data["phone"]).count()
        if phone_count == 1 and data["phone"] != user.phone:
            flash("手机号已经存在！", "err")
            return redirect(url_for("home.user", form=form, user=user))
        user.name = data["name"]
        user.email = data["email"]
        user.phone = data["phone"]
        user.info = data["info"]
        user.save()
        flash("资料更新成功！", "ok")
        return redirect(url_for(".user"))
    return render_template('home/user/profile.html', form=form, user=user)


@main.route('/pwd/', methods=['GET', 'POST'])
@user_login_req
def pwd():
    form = PwdForm()
    if form.validate_on_submit():
        data = form.data
        user = User.query.filter_by(name=session["user"]).first()
        user.pwd = generate_password_hash(data["new_pwd"])
        user.save()
        flash("密码修改成功！请重新登录", "ok")
        return redirect(url_for("index.login"))
    return render_template('home/user/pwd.html', form=form)


@main.route('/comment/<int:page>/', methods=['GET'])
@user_login_req
def comment(page=None):
    if page == None:
        page = 1
    page_data = Comment.query.join(User).filter(
        Comment.user_id == User.id,
        User.name == session["user"]
    ).order_by(
        Comment.addtime.desc()
    ).paginate(page=page, per_page=10)
    return render_template('home/user/comment.html', page_data=page_data)


@main.route('/loginlog/<int:page>/', methods=['GET'])
@user_login_req
def loginlog(page=None):
    if page == None:
        page = 1
    page_data = Userlog.query.join(User).filter(
        User.id == Userlog.user_id,
        User.name == session["user"]
    ).order_by(
        Userlog.addtime.desc()
    ).paginate(page=page, per_page=10)
    return render_template('home/user/loginlog.html', page_data=page_data)


@main.route('/moviecol/<int:page>/', methods=['GET'])
@user_login_req
def moviecol(page=None):
    if page == None:
        page = 1
    page_data = Moviecol.query.join(User).join(Movie).filter(
        User.id == Moviecol.user_id,
        Movie.id == Moviecol.movie_id,
        User.name == session["user"]
    ).order_by(
        Moviecol.addtime.desc()
    ).paginate(page=page, per_page=10)
    return render_template('home/user/moviecol.html', page_data=page_data)


@main.route("/moviecol/add/", methods=["GET"])
@user_login_req
def moviecol_add():
    import json
    mid = request.args.get("mid", '')
    uid = request.args.get("uid", '')
    moviecol_count = Moviecol.query.filter(
        Moviecol.movie_id == int(mid),
        Moviecol.user_id == int(uid),
    ).count()
    if moviecol_count == 1:
        data = dict(ok=0)
    if moviecol_count == 0:
        data = dict(ok=1)
        form = dict(
            movie_id=int(mid),
            user_id=int(uid),
        )
        moviecol = Moviecol(form)
        moviecol.save()
    return json.dumps(data)

