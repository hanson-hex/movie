# -*- encoding=utf-8 -*-
from flask import Flask
from flask import render_template
from flask import Blueprint
from flask import redirect
from flask import url_for
from . import admin_login_req
from app.models.user import User
from flask import flash
from . import admin_auth

main = Blueprint('admin_user', __name__)


@main.route('/list/<int:page>/', methods=['GET'])
@admin_auth
@admin_login_req
def list(page=None):
    if page == None:
        page = 1
    page_data = User.query.order_by(
        User.addtime.desc()
    ).paginate(page=page, per_page=10)
    return render_template('admin/user/list.html', page_data=page_data)


@main.route('/view/<int:id>/', methods=['GET'])
@admin_login_req
def view(id=None):
    user = User.query.filter_by(id=id).first_or_404()
    return render_template('admin/user/view.html', user=user)


# 删除会员
@main.route("/delete/<int:id>/", methods=["GET"])
@admin_auth
@admin_login_req
def delete(id=None):
    user = User.query.filter_by(id=id). first_or_404()
    user.delete()
    flash("删除会员成功！", "ok")
    return redirect(url_for(".list", page=1))