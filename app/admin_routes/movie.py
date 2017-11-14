# -*- encoding=utf-8 -*-
from flask import Flask
from flask import render_template
from flask import Blueprint
from flask import redirect
from flask import url_for
from . import admin_login_req

main = Blueprint('movie', __name__)


@main.route('/add/')
@admin_login_req
def add():
    return render_template('admin/movie/add.html')


@main.route('/list/')
@admin_login_req
def list():
    return render_template('admin/movie/list.html')