# -*- encoding=utf-8 -*-
from flask import Flask
from flask import render_template
from flask import Blueprint
from flask import redirect
from flask import url_for
from . import admin_login_req


main = Blueprint('moviecol', __name__)


@main.route('/list/')
@admin_login_req
def list():
    return render_template('admin/moviecol/list.html')