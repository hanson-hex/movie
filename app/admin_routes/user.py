# -*- encoding=utf-8 -*-
from flask import Flask
from flask import render_template
from flask import Blueprint
from flask import redirect
from flask import url_for

main = Blueprint('admin_user', __name__)


@main.route('/list/')
def list():
    return render_template('admin/user/list.html')


@main.route('/view/')
def view():
    return render_template('admin/user/view.html')