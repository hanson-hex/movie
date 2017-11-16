# -*- encoding=utf-8 -*-
from flask import Flask
from flask import render_template
from flask import Blueprint
from flask import redirect
from flask import url_for
from . import admin_login_req
from app.models.role import Role
from flask import flash
from flask import request
from app.admin_routes.forms import RoleForm
from app.utils import log
from . import admin_auth

main = Blueprint('role', __name__)


@main.route("/add/", methods=["GET", "POST"])
@admin_auth
@admin_login_req
def add():
    form = RoleForm()
    if form.validate_on_submit():
        data = form.data
        role = Role.query.filter_by(name=data['name']).count()
        if role == 1:
            flash("角色已经存在！", "err")
            return redirect(url_for("role.add"))
        role = Role(data)
        role.save()
        flash("角色添加成功！", "ok")
        redirect(url_for('role.add'))
    return render_template('admin/role/add.html', form=form)


# 角色列表
@main.route("/list/<int:page>/", methods=["GET"])
# @admin_auth
@admin_login_req
def list(page=None):
    if page == None:
        page = 1
    page_data = Role.query.order_by(
        Role.addtime.desc()
    ).paginate(page=page, per_page=10)
    return render_template('admin/role/list.html', page_data=page_data)


# 编辑角色
@main.route("/edit/<int:id>/", methods=["GET","POST"])
# @admin_auth
@admin_login_req
def edit(id=None):
    form = RoleForm()
    role = Role.query.get_or_404(id)
    if request.method == "GET":
        log('role.auth', role.auths)
        list_auths = role.auths.split(',')
        temp = []
        for i in list_auths:
            temp.append(int(i))
        form.auths.data = temp
        log('temp', temp)
    if form.validate_on_submit():
        data = form.data
        role_count = Role.query.filter_by(name=data['name']).count()
        if role.name != data["name"] and role_count == 1:
            flash("角色已经存在！", "err")
            return redirect(url_for("role.edit", id=id))
        role.name = data["name"]
        stemp = []
        for i in data["auths"]:
            stemp.append(str(i))
        role.auths = ','.join(stemp)
        role.save()
        flash("标签修改成功！", "ok")
        redirect(url_for('role.edit', id=id))
    return render_template('admin/role/edit.html', form=form, role=role)


# 角色删除
@main.route("/delete/<int:id>/", methods=["GET"])
@admin_auth
@admin_login_req
def delete(id=None):
    role = Role.query.filter_by(id=id). first_or_404()
    role.delete()
    flash("删除角色成功！", "ok")
    return redirect(url_for("role.list", page=1))


