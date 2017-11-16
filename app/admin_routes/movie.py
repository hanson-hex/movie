# -*- encoding=utf-8 -*-
from flask import Flask
from flask import render_template
from flask import Blueprint
from flask import redirect
from flask import url_for
from . import admin_login_req
from app.admin_routes.forms import MovieForm
from app.models.movie import Movie
from app import app
from werkzeug.utils import secure_filename
from flask import flash
from datetime import datetime
import uuid
import os
from app.utils import log
from flask import request
from . import admin_auth

main = Blueprint('movie', __name__)


def change_filename(filename):
    fileinfo = os.path.splitext(filename)
    newname = datetime.now().strftime("%Y%m%d%H%M%S") + str(uuid.uuid4().hex) + fileinfo[-1]
    return newname


def saved_file(path, data):
    log('开始保存')
    if not os.path.exists(path):
        os.makedirs(path)
        os.chmod(path,  'rw')
    filename = secure_filename(data.filename)
    newname = change_filename(filename)
    data.save(path + newname)
    return newname


@main.route('/add/', methods=['GET', 'POST'])
@admin_auth
@admin_login_req
def add():
    form = MovieForm()
    log('进入添加电影路由')
    if form.validate_on_submit():
        data = form.data
        log('输入不为空')
        movie_count = Movie.query.filter_by(title=data['title']).count()
        if movie_count == 1:
            flash("片名已经存在！", "err")
            return redirect(url_for(".add", form=form))
        path = app.config['UP_DIR']
        log('data', data)
        log('form.logo', form.logo)
        log('form.logo.data', form.logo.data)
        log('form.logo.data.filename', form.logo.data.filename)
        url = saved_file(path, form.url.data)
        logo = saved_file(path, form.logo.data)
        movie = Movie(data)
        movie.url = url
        movie.logo = logo
        movie.save()
        flash('添加电影成功！', 'ok')
        return redirect(url_for('.add'))
    return render_template('admin/movie/add.html', form=form)


@main.route('/list/<int:page>/', methods=['GET'])
@admin_auth
@admin_login_req
def list(page=None):
    if page == None:
        page = 1
    # 按时间顺序获得电影数据
    page_data = Movie.query.order_by(
        Movie.addtime.desc()
    ).paginate(page=page, per_page=10)
    return render_template('admin/movie/list.html', page_data=page_data)


@main.route('/delete/<int:id>/', methods=['GET'])
@admin_auth
@admin_login_req
def delete(id):
    """
    删除电影
    """
    movie = Movie.query.filter_by(id=id).first_or_404()
    movie.delete()
    flash('删除电影成功！', 'ok')
    return redirect(url_for('.list', page=1))


@main.route('/edit/<int:id>/', methods=['GET', 'POST'])
@admin_auth
@admin_login_req
def edit(id):
    """
    编辑电影
    """
    form = MovieForm()
    # 查找系统需要编辑的电影
    movie = Movie.query.filter_by(id=id).first_or_404()
    # 给验证器置0， 否则会报错
    form.url.validators = []
    form.logo.validators = []
    if request.method =="GET":
        form.info.data = movie.info
        form.tag_id.data = movie.tag_id
        form.star.data = movie.star
    if form.validate_on_submit():
        data = form.data
        movie_count = Movie.query.filter_by(title=data['title']).count()
        # 若修改的电影名称已存在在系统上， 显示错误信息
        if movie_count == 1 and movie.title != data['title']:
            flash('电影名称已经存在！', 'err')
            return redirect(url_for('.edit', id=movie.id))
        else:
            path = app.config['UP_DIR']
            if form.url.data.filename != '':
                url = saved_file(path, form.url.data)
                movie.url = url
            if form.logo.data.filename != '':
                logo = saved_file(path, form.logo.data)
                movie.logo = logo
            movie.title = data["title"]
            movie.info = data["info"]
            movie.length = data["length"]
            movie.star = data["star"]
            movie.tag_id = data["tag_id"]
            movie.area = data["area"]
            movie.release_time = data["release_time"]
            movie.save()
            flash('编辑电影成功！', 'ok')
            return redirect(url_for('.edit', id=movie.id))
    log('movie url', movie.url)
    return render_template('admin/movie/edit.html', form=form, movie=movie)
