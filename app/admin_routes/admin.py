# -*- encoding=utf-8 -*-
from flask import Flask
from flask import render_template
from flask import Blueprint
from flask import redirect
from flask import url_for
from . import admin_login_req
from app.models.admin import Admin
from app.admin_routes.forms import AdminForm
from flask import flash
from app.models.role import Role
from app.admin_routes.forms import PwdForm
from . import admin_auth

main = Blueprint('administrator', __name__)


@main.route("/add/", methods=["GET", "POST"])
@admin_auth
@admin_login_req
def add():
    form = AdminForm()
    if form.validate_on_submit():
        data = form.data
        admin_count = Admin.query.filter_by(name=data["name"]).count()
        if admin_count == 1:
            flash("管理员已经存在", 'err')
            return redirect(url_for('.add'))
        admin = Admin(data)
        admin.save()
        flash("管理员添加成功！", "ok")
        redirect(url_for('.add'))
    return render_template('admin/administrator/add.html', form=form)


# 管理员列表
@main.route("/list/<int:page>/", methods=["GET", "POST"])
@admin_auth
@admin_login_req
def list(page=None):
    if page == None:
        page = 1
    page_data = Admin.query.join(Role).filter(
        Role.id == Admin.role_id,
    ).order_by(
        Admin.addtime.desc()
    ).paginate(page=page, per_page=10)
    return render_template('admin/administrator/list.html', page_data=page_data)


