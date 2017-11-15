# -*- encoding=utf-8 -*-
from flask import Flask
from flask import render_template
from flask import Blueprint
from flask import redirect
from flask import url_for
from . import admin_login_req
from app.admin_routes.forms import TagForm
from app.models.tag import Tag
from flask import flash
from flask import session
from app.utils import log




main = Blueprint('tag', __name__)



@main.route('/add/', methods=['GET', 'POST'])
@admin_login_req
def add():
    """
    添加标签
    """
    form = TagForm()
    # 判断表单是否为空
    if form.validate_on_submit():
        data = form.data
        tag = Tag.query.filter_by(name=data['name']).count()
        log('tag', tag)
        # 若标签名称存在， 则返回错误信息
        if tag == 1:
            flash('标签名称已经存在！', 'err')
            return redirect(url_for('tag.add'))
        # 若名称不存在， 则添加
        else:
            tag = Tag(data)
            tag.save()
            flash('标签添加成功', 'ok')
            return redirect(url_for('tag.add'))
    return render_template('admin/tag/add.html', form=form)

@main.route('/list/<int:page>', methods=['GET'])
@admin_login_req
def list(page=None):
    """
    标签列表
    """
    if page == None:
        page = 1
    # 按添加时间获得标签数据
    page_data = Tag.query.order_by(
        Tag.addtime.desc()
    ).paginate(page=page, per_page=10)
    return render_template('admin/tag/list.html', page_data=page_data)


@main.route('/delete/<int:id>/', methods=['GET'])
@admin_login_req
def delete(id):
    """
    删除标签
    """
    tag = Tag.query.filter_by(id=id).first_or_404()
    tag.delete()
    flash('删除标签成功！', 'ok')
    return redirect(url_for('.list', page=1))


@main.route('/edit/<int:id>', methods=['GET', 'POST'])
@admin_login_req
def edit(id):
    """
    编辑标签
    """
    form = TagForm()
    # 查找系统存在的标签
    tag = Tag.query.filter_by(id=id).first_or_404()
    if form.validate_on_submit():
        data = form.data
        tag_count = Tag.query.filter_by(name=data['name']).count()
        # 若修改的标签已存在在系统上， 删除标签
        if tag_count == 1 and tag.name != data['name']:
            flash('标签名称已经存在！', 'err')
            return redirect(url_for('tag.edit'))
        else:
            tag.name=data['name']
            tag.save()
            flash('标签修改成功', 'ok')
            return redirect(url_for('tag.edit'))
    return render_template('admin/tag/edit.html', form=form, tag=tag)