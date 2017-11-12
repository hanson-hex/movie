# -*- encoding=utf-8 -*-
from flask import Flask
from flask import render_template
from flask import Blueprint
from flask import redirect
from flask import url_for

main = Blueprint('user', __name__)

@main.route('/')
def user():
    return redirect(url_for('.profile'))


@main.route('/profile/')
def profile():
    return render_template('home/user/profile.html')


@main.route('/pwd/')
def pwd():
    return render_template('home/user/pwd.html')


@main.route('/comment/')
def comment():
    return render_template('home/user/comment.html')


@main.route('/loginlog/')
def loginlog():
    return render_template('home/user/loginlog.html')


@main.route('/moviecol/')
def moviecol():
    return render_template('home/user/moviecol.html')