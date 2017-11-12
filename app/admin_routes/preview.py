# -*- encoding=utf-8 -*-
from flask import Flask
from flask import render_template
from flask import Blueprint
from flask import redirect
from flask import url_for

main = Blueprint('preview', __name__)


@main.route('/add/')
def add():
    return render_template('admin/preview/add.html')


@main.route('/list/')
def list():
    return render_template('admin/preview/list.html')