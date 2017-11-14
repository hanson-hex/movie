# -*- encoding=utf-8 -*-
from flask import Flask
from flask import render_template
from flask import Blueprint
from flask import redirect
from flask import url_for
from . import admin_login_req

main = Blueprint('log', __name__)



@main.route('/optlog/list/')
@admin_login_req
def optlog_list():
    return render_template('admin/log/optlog_list.html')



@main.route('/adminloginlog/list/')
@admin_login_req
def adminloginlog_list():
    return render_template('admin/log/adminloginlog_list.html')


@main.route('/userloginlog/list/')
@admin_login_req
def userloginlog_list():
    return render_template('admin/log/userloginlog_list.html')