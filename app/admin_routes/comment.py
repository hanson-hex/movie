# -*- encoding=utf-8 -*-
from flask import Flask
from flask import render_template
from flask import Blueprint
from flask import redirect
from flask import url_for
from . import admin_login_req
from app.models.comment import Comment
from app.models.movie import Movie
from app.models.user import User
from flask import flash
from . import admin_auth

main = Blueprint('comment', __name__)


@main.route('/list/<int:page>/', methods=['GET'])
@admin_auth
@admin_login_req
def list(page=None):
    if page == None:
        page = 1
    page_data = Comment.query.join(Movie).join(User).filter(
        Movie.id == Comment.movie_id,
        User.id == Comment.user_id,
    ).order_by(
        Comment.addtime.desc()
    ).paginate(page=page, per_page=10)
    return render_template('admin/comment/list.html', page_data=page_data)


@main.route("/delete/<int:id>/", methods=["GET"])
@admin_auth
@admin_login_req
def delete(id=None):
    comment = Comment.query.filter_by(id=id). first_or_404()
    comment.delete()
    flash("删除评论成功！", "ok")
    return redirect(url_for(".list", page=1))
