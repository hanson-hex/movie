# -*- encoding=utf-8 -*-
from flask import Flask
from flask import render_template
from flask import Blueprint
from flask import redirect
from flask import url_for

main = Blueprint('admin', __name__)


@main.route('/')
def index():
    return render_template('admin/index.html')

@main.route('/pwd/')
def pwd():
    return render_template('admin/pwd.html')

@main.route('/login/')
def login():
    return render_template('admin/login.html ')


@main.route('/logout/')
def logout():
    return redirect(url_for('.login'))
