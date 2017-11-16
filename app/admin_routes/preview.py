# -*- encoding=utf-8 -*-
from flask import Flask
from flask import render_template
from flask import Blueprint
from flask import redirect
from flask import url_for
from . import admin_login_req
from app.models.preview import Preview
from app.admin_routes.forms import PreviewForm
from flask import flash
from app.admin_routes.movie import saved_file
from app import app
from app.utils import log
import os
from werkzeug.utils import secure_filename
from app.admin_routes.movie import change_filename
from . import admin_auth

main = Blueprint('preview', __name__)





@main.route('/add/', methods=['GET', 'POST'])
@admin_auth
@admin_login_req
def add():
    form = PreviewForm()
    if form.validate_on_submit():
        data = form.data
        preview_count = Preview.query.filter_by(title=data['title']).count()
        if preview_count == 1:
            flash("预告标题已经存在！", "err")
            return redirect(url_for(".add"))
        path = app.config["UP_DIR"]
        log('form.logo.data', form.logo.data)
        logo = saved_file(path, form.logo.data)
        preview = Preview(data)
        preview.logo = logo
        preview.save()
        flash("预告添加成功！", "ok")
        redirect(url_for('.add'))
    return render_template('admin/preview/add.html', form=form)


@main.route('/list/<int:page>/', methods=["GET", "POST"])
@admin_auth
@admin_login_req
def list(page=None):
    if page == None:
        page = 1
    page_data = Preview.query.order_by(
        Preview.addtime.desc()
    ).paginate(page=page, per_page=10)
    return render_template('admin/preview/list.html', page_data=page_data)


@main.route('/edit/<int:id>', methods=['GET', 'POST'])
@admin_auth
@admin_login_req
def edit(id):
    form = PreviewForm()
    preview = Preview.query.filter_by(id=id).first_or_404()
    log('preview', preview)
    form.logo.validators = []
    if form.validate_on_submit():
        data = form.data
        preview_count = Preview.query.filter_by(title=data['title']).count()
        if preview_count == 1 and preview.title != data['title']:
            flash("预告标题已经存在！", "err")
            return redirect(url_for(".edit", id=preview.id))
        preview.title = data['title']
        if form.logo.data.filename != '':
            path = app.config["UP_DIR"]
            log('form.logo.data', form.logo.data)
            logo = saved_file(path, form.logo.data)
            preview.logo = logo
        preview.save()
        flash("预告编辑成功！", "ok")
        redirect(url_for('.edit', id=preview.id))
    # log('preview logo', preview.logo)
    # log('preview title', preview.title)
    return render_template('admin/preview/edit.html', form=form, preview=preview)

@main.route('/delete/<int:id>/', methods=['GET'])
@admin_auth
@admin_login_req
def delete(id):
    """
    删除电影
    """
    preview = Preview.query.filter_by(id=id).first_or_404()
    preview.delete()
    flash('删除预告成功！', 'ok')
    return redirect(url_for('.list', page=1))
