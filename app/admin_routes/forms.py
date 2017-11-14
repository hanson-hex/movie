# -*- encoding=utf-8 -*-

from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import FileField
from wtforms import TextAreaField
from wtforms import PasswordField
from wtforms import SubmitField
from wtforms import SelectField
from wtforms import SelectMultipleField

from wtforms.validators import DataRequired
from wtforms.validators import ValidationError
from wtforms.validators import EqualTo
from app.models.admin import Admin
from app.models.tag import Tag
from app.models.auth import Auth
from app.models.role import Role
from app.models.movie import Movie
from app.models.adminlog import Adminlog
from app.models.moviecol import Moviecol
from app.models.userlog import Userlog
from app.models.comment import Comment
from app.models.user import User
from app.models.preview import Preview
from app.models.oplog import Oplog
from app.models.userlog import Userlog

from flask import session

from werkzeug.security import check_password_hash

tags = Tag.query.all()
auth_list = Auth.query.all()
roles = Role.query.all()

class LoginForm(FlaskForm):
    """管理员登录表单"""
    name = StringField(
        label='帐号',
        validators=[
            DataRequired("请输入帐号！")
        ],
        description="账户",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入账号！",
            # "required": "required"
        },
    )
    pwd = PasswordField(
        label='密码',
        validators=[
            DataRequired("请输入密码！")
        ],
        description="密码",
        render_kw={
        "class" : "form-control",
        "placeholder" : "请输入密码！",
        # "required" : "required"
        }
    )
    submit = SubmitField(
        label='登录',
        render_kw={

    "class" : "btn btn-primary btn-block btn-flat"
        }
    )

    def validate_account(self, field):
        username = field.data
        admin = Admin.find_by(name=username)
        if admin == None:
            raise ValidationError("帐号不存在!")


class TagForm(FlaskForm):
    """标签表单"""
    name = StringField(
        label='标签',
        validators=[
            DataRequired("请输入标签！")
        ],
        description="标签",
        render_kw={
            "class":"form-control",
            "id":"input_name",
            "placeholder":"请输入标签名称！"
        },
    )
    submit = SubmitField(
        label='编辑',
        render_kw={

            "class": "btn btn-primary"
        }
    )


class MovieForm(FlaskForm):
    """电影表单"""
    title = StringField(
        label='片名',
        validators=[
            DataRequired("请输入片名！")
        ],
        description="片名",
        render_kw={
            "class": "form-control",
            "id": "input_title",
            "placeholder": "请输入片名！"
        },
    )
    url = FileField(
        label='文件',
        validators=[
            DataRequired("请输入文件'！")
        ],
        description="文件",
        render_kw={
            "id": "input_url",
        },
    )
    info = TextAreaField(
        label='简介',
        validators=[
            DataRequired("请输入简介'！")
        ],
        description="简介",
        render_kw={
            "class": "form-control",
            "rows":"10"
        },
    )
    logo = FileField(
        label='封面',
        validators=[
            DataRequired("请输入封面'！")
        ],
        description="封面",
        render_kw={
            "id": "input_logo",
        },
    )
    star = SelectField(
        label='星级',
        validators=[
            DataRequired("请输入星级'！")
        ],
        coerce=int,
        choices=[(1,"1星"),(2,"2星"),(3,"3星"),(4,"4星"),(5,"5星")],
        description="星级",
        render_kw={
            "class": "form-control",
            "id": "input_star",
        },
    )
    tag_id = SelectField(
        label='标签',
        validators=[
            DataRequired("请输入标签！")
        ],
        coerce=int,
        choices=[(v.id, v.name) for v in tags],
        description="标签",
        render_kw={
            "class": "form-control",
            "id": "input_tag_id",
        },
    )
    area = StringField(
        label='地区',
        validators=[
            DataRequired("请输入地区'！")
        ],
        description="地区",
        render_kw={
            "class": "form-control",
            "id": "input_area",
            "placeholder": "请输入地区！"
        },
    )
    length = StringField(
        label='时长',
        validators=[
            DataRequired("请输入时长！")
        ],
        description="时长",
        render_kw={
            "class": "form-control",
            "id": "input_length",
            "placeholder": "请输入时长！"
        },
    )
    release_time = StringField(
        label='放映时间',
        validators=[
            DataRequired("放映时间！")
        ],
        description="放映时间",
        render_kw={
            "class": "form-control",
            "id": "input_release_time",
            "placeholder": "放映时间！"
        },
    )
    submit = SubmitField(
        label='编辑',
        render_kw={
            "class": "btn btn-primary"
        }
    )


class PreviewForm(FlaskForm):
    """预告表单"""
    title = StringField(
        label='预告标题',
        validators=[
            DataRequired("请输入预告标题！")
        ],
        description="预告标题",
        render_kw={
            "class": "form-control",
            "id": "input_title",
            "placeholder": "请输入预告标题！"
        },
    )
    logo = FileField(
        label='预告封面',
        validators=[
            DataRequired("请输入预告封面'！")
        ],
        description="预告封面",
        render_kw={
            "id": "input_logo",
        },
    )
    submit = SubmitField(
        label='编辑',
        render_kw={

            "class": "btn btn-primary"
        }
    )


class PwdForm(FlaskForm):
    """密码表单"""
    old_pwd = PasswordField(
        label='旧密码',
        validators=[
            DataRequired("请输入旧密码！")
        ],
        description="旧密码",
        render_kw={
        "class" : "form-control",
        "placeholder" : "请输入旧密码！",
            "id": "input_pwd",
        # "required" : "required"
        }
    )
    new_pwd = PasswordField(
        label='新密码',
        validators=[
            DataRequired("请输入新密码！")
        ],
        description="新密码",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入新密码！",
            "id": "input_newpwd",
            # "required" : "required"
        }
    )
    submit = SubmitField(
        label='修改',
        render_kw={
            "class": "btn btn-primary"
        }
    )

    def validate_old_pwd(self, field):
        pwd = field.data
        name = session['admin']
        admin = Admin.query.filter_by(name=name).first()
        if not admin.check_pwd(pwd):
            raise ValidationError("旧密码错误!")


class AuthForm(FlaskForm):
    """权限表单"""
    name = StringField(
        label='权限名称',
        validators=[
            DataRequired("请输入权限名称！")
        ],
        description="权限名称",
        render_kw={
            "class": "form-control",
            "id": "input_name",
            "placeholder": "请输入权限名称！"
        },
    )
    url = StringField(
        label='权限地址',
        validators=[
            DataRequired("请输入权限地址'！")
        ],
        description="权限地址",
        render_kw={
            "class": "form-control",
            "id": "input_url",
            "placeholder": "请输入权限地址！"
        },
    )
    submit = SubmitField(
        label='编辑',
        render_kw={

            "class": "btn btn-primary"
        }
    )


class RoleForm(FlaskForm):
    """角色表单"""
    name = StringField(
        label='角色名称',
        validators=[
            DataRequired("请输入角色名称！")
        ],
        description="角色名称",
        render_kw={
            "class": "form-control",
            "id": "input_name",
            "placeholder": "请输入角色名称！"
        },
    )
    auths = SelectMultipleField(
        label='操作权限',
        validators=[
            DataRequired("请选择权限！")
        ],
        coerce=int,
        choices=[(v.id, v.name) for v in auth_list],
        description="操作权限",
        render_kw={
            "class": "form-control",
            "id": "input_auths",
            "placeholder": "请选择权限！"
        },
    )
    submit = SubmitField(
        label='编辑',
        render_kw={

            "class": "btn btn-primary"
        }
    )


class AdminForm(FlaskForm):
    """管理员表单"""
    name = StringField(
        label='管理员名称',
        validators=[
            DataRequired("请输入管理员名称！")
        ],
        description="管理员名称",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入管理员名称！",
            "id": "input_name",
            # "required": "required"
        },
    )
    pwd = PasswordField(
        label='管理员密码',
        validators=[
            DataRequired("请输入管理员密码")
        ],
        description="管理员密码",
        render_kw={
        "class" : "form-control",
        "placeholder" : "请输入管理员密码!",
        # "required" : "required"
        }
    )
    repeat_pwd =  PasswordField(
        label='管理员重复密码',
        validators=[
            DataRequired("请输入管理员重复密码！"),
            EqualTo('pwd', message="两次密码不一致")
        ],
        description="管理员重复密码",
        render_kw={
        "class" : "form-control",
        "placeholder" : "请输入管理员重复密码！",
        # "required" : "required"
        }
    )
    submit = SubmitField(
        label='编辑',
        render_kw={
    "class" : "btn btn-primary btn-block btn-flat"
        }
    )

    role_id = SelectField(
        label='管理员角色',
        validators=[
            DataRequired("请输入管理员角色！")
        ],
        coerce=int,
        choices=[(v.id, v.name) for v in roles],
        description="管理员角色",
        render_kw={
            "class": "form-control",
            "id": "input_role_id",
        },
    )




