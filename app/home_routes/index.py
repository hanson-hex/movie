# -*- encoding=utf-8 -*-
from flask import Flask
from flask import render_template
from flask import Blueprint
from flask import redirect
from flask import url_for

main = Blueprint('index', __name__)


@main.route('/')
def index():
    return render_template('home/index.html ')


@main.route('/animation/')
def animation():
    return render_template('home/animation.html')


@main.route('/search/')
def search():
    return render_template('home/search.html')


@main.route('/play/')
def play():
    return render_template('home/play.html')


@main.route('/login/')
def login():
    return render_template('home/login.html')


@main.route('/logout/')
def logout():
    return redirect(url_for('.login'))


@main.route('/register/')
def register():
    return render_template('home/register.html')




