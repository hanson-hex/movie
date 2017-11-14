# -*- encoding=utf-8 -*-
from flask import Flask
from flask import render_template
from flask import Blueprint
from flask import redirect
from flask import url_for
from flask import flash
from flask import session
from flask import request

from . import admin_login_req

from app.utils import log

from app.models.admin import Admin

from functools import wraps

from app.admin_routes.forms import LoginForm

main = Blueprint('admin', __name__)



@main.route('/')
@admin_login_req
def index():
    return render_template('admin/index.html', )


@main.route('/pwd/')
@admin_login_req
def pwd():
    return render_template('admin/pwd.html')


@main.route('/login/', methods=['GET', 'POST'])
def login():
    """
    后台登录
    """
    form = LoginForm()
    # 判断用户是否输入为空
    if form.validate_on_submit():
        data = form.data
        # 查询管理员
        admin = Admin.query.filter_by(name=data['name']).first()
        # 若无，说明管理员用户名错误
        if not admin:
            flash('管理员用户名错误', 'err')
            return redirect(url_for('admin.login'))
        log('admin', admin)
        # 若有，校验密码是否正确
        if not admin.check_pwd(data['pwd']):
            log('密码错误')
            flash('密码错误', "err")
            return redirect(url_for('admin.login'))
        session['admin'] = data['name']
        return redirect(request.args.get('next') or url_for('admin.index'))
    return render_template('admin/login.html ', form=form)



@main.route('/logout/')
@admin_login_req
def logout():
    session.pop('admin')
    return redirect(url_for('.login'))
