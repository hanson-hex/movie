# -*- encoding=utf-8 -*-
from flask import Flask
from flask import render_template
from flask import Blueprint
from flask import redirect
from flask import url_for
from . import admin_login_req
from app.models.oplog import Oplog
from app.models.admin import Admin
from app.models.adminlog import Adminlog
from app.models.userlog import Userlog
from app.models.user import User
from . import admin_auth

main = Blueprint('log', __name__)


# 操作日志
@main.route("/optlog/list/<int:page>/", methods=["GET"])
@admin_auth
@admin_login_req
def optlog_list(page=None):
    if page == None:
        page = 1
    page_data = Oplog.query.join(Admin).filter(
        Admin.id == Oplog.admin_id
    ).order_by(
        Oplog.addtime.desc()
    ).paginate(page=page, per_page=10)
    return render_template('admin/log/optlog_list.html', page_data=page_data)


# 管理员登录日志
@main.route("/adminloginlog/list/<int:page>/", methods=["GET"])
@admin_auth
@admin_login_req
def adminloginlog_list(page=None):
    if page == None:
        page = 1
    page_data = Adminlog.query.join(Admin).filter(
        Admin.id == Adminlog.admin_id
    ).order_by(
        Adminlog.addtime.desc()
    ).paginate(page=page, per_page=10)
    return render_template('admin/log/adminloginlog_list.html', page_data=page_data)


# 会员登录日志
@main.route("/userloginlog/list/<int:page>/", methods=["GET"])
@admin_auth
@admin_login_req
def userloginlog_list(page=None):
    if page == None:
        page = 1
    page_data = Userlog.query.join(User).filter(
        User.id == Userlog.user_id
    ).order_by(
        Userlog.addtime.desc()
    ).paginate(page=page, per_page=10)
    return render_template('admin/log/userloginlog_list.html', page_data=page_data)