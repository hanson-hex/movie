# -*- encoding=utf-8 -*-
from flask import Flask
from flask import render_template
from flask import Blueprint
from flask import redirect
from flask import url_for
from . import admin_login_req
from app.admin_routes.forms import AuthForm
from app.models.auth import Auth
from flask import flash
from . import admin_auth

main = Blueprint('auth', __name__)


# 添加权限
@main.route("/add/", methods=["GET", "POST"])
# @admin_auth
@admin_login_req
def add():
    form = AuthForm()
    if form.validate_on_submit():
        data = form.data
        auth = Auth.query.filter_by(name=data['name']).count()
        if auth == 1:
            flash("权限已经存在！", "err")
            return redirect(url_for("auth.add"))
        auth = Auth(data)
        auth.save()
        flash("标签添加成功！", "ok")
        redirect(url_for('.add'))
    return render_template('admin/auth/add.html', form=form)


# 权限列表
@main.route("/auth/list/<int:page>/", methods=["GET"])
# @admin_auth
@admin_login_req
def list(page=None):
    if page == None:
        page = 1
    page_data = Auth.query.order_by(
        Auth.addtime.desc()
    ).paginate(page=page, per_page=10)
    return render_template('admin/auth/list.html', page_data=page_data)


# 权限删除
@main.route("/auth/delete/<int:id>/", methods=["GET"])
# @admin_auth
@admin_login_req
def delete(id=None):
    auth = Auth.query.filter_by(id=id). first_or_404()
    auth.delete()
    flash("删除权限成功！", "ok")
    return redirect(url_for("auth.list", page=1))


# 权限编辑
@main.route("/auth/edit/<int:id>/", methods=["GET","POST"])
# @admin_auth
@admin_login_req
def edit(id=None):
    form = AuthForm()
    auth = Auth.query.get_or_404(id)
    if form.validate_on_submit():
        data = form.data
        auth_count = Auth.query.filter_by(name=data['name']).count()
        if auth.name != data["name"] and auth_count == 1:
            flash("权限已经存在！", "err")
            return redirect(url_for("auth.edit", id=id))
        auth.name = data["name"]
        auth.url = data["url"]
        auth.save()
        flash("权限修改成功！", "ok")
        redirect(url_for('auth.edit', id=id))
    return render_template('admin/auth/edit.html', form=form, auth=auth)

