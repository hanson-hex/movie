# -*- encoding=utf-8 -*-
from flask import Flask
from flask import render_template
from flask import Blueprint
from flask import redirect
from flask import url_for
from . import admin_login_req
from app.models.user import User
from app.models.movie import Movie
from app.models.moviecol import Moviecol
from flask import flash
from . import admin_auth

main = Blueprint('moviecol', __name__)


@main.route('/list/<int:page>/', methods=['GET'])
@admin_auth
@admin_login_req
def list(page=None):
    if page == None:
        page = 1
    page_data = Moviecol.query.join(User).join(Movie).filter(
        User.id == Moviecol.user_id,
        Movie.id == Moviecol.movie_id
    ).order_by(
        Moviecol.addtime.desc()
    ).paginate(page=page, per_page=10)
    return render_template('admin/moviecol/list.html', page_data=page_data)


@main.route("/delete/<int:id>/", methods=["GET"])
@admin_auth
@admin_login_req
def delete(id=None):
    moviecol = Moviecol.query.filter_by(id=id). first_or_404()
    moviecol.delete()
    flash("删除收藏成功！", "ok")
    return redirect(url_for(".list", page=1))