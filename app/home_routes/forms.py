# -*- encoding=utf-8 -*-
from flask import session

from flask_wtf import FlaskForm

from wtforms.fields import StringField
from wtforms import PasswordField
from wtforms import SubmitField
from wtforms import TextAreaField
from wtforms import FileField

from wtforms.validators import DataRequired
from wtforms.validators import EqualTo
from wtforms.validators import email
from wtforms.validators import Regexp
from wtforms.validators import ValidationError

from app.models.user import User


class UserForm(FlaskForm):
    """会员表单"""
    name = StringField(
        label='昵称',
        validators=[
            DataRequired("请输入昵称！")
        ],
        description="昵称",
        render_kw={
            "class": "form-control",
            "placeholder": "昵称！",
            # "required": "required"
        },
    )
    email = StringField(
        label='邮箱',
        validators=[
            DataRequired("请输入邮箱！"),
            email("邮箱格式不正确!")
        ],
        description="邮箱",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入邮箱！",
            # "required": "required"
        },
    )
    phone = StringField(
        label='手机号',
        validators=[
            DataRequired("请输入手机号！"),
            Regexp("^1[3458]\d{9}$", message="手机号格式错误")
        ],
        description="手机号",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入手机号！",
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
    rep_pwd = PasswordField(
        label='确认密码',
        validators=[
            DataRequired("请输入确认密码！"),
            EqualTo('pwd', message="两次密码不一致")
        ],
        description="确认密码",
        render_kw={
        "class" : "form-control",
        "placeholder" : "请输入确认密码！",
        # "required" : "required"
        }
    )
    submit = SubmitField(
        label='注册',
        render_kw={

    "class" : "btn btn-lg btn-success btn-block"
        }
    )

    def validate_name(self, field):
        name = field.data
        user = User.query.filter_by(name=name).count()
        if user == 1:
            raise ValidationError("昵称已经存在！")

    def validate_email(self, field):
        email = field.data
        user = User.query.filter_by(email=email).count()
        if user == 1:
            raise ValidationError("邮箱已经存在！")

    def validate_phone(self, field):
        phone = field.data
        user = User.query.filter_by(phone=phone).count()
        if user == 1:
            raise ValidationError("手机号已经存在！")


class LoginForm(FlaskForm):
    """会员登录表单"""
    name = StringField(
        label='帐号',
        validators=[
            DataRequired("请输入帐号！")
        ],
        description="账号",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入帐号！",
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
            "class": "form-control",
            "placeholder": "密码",
            # "required" : "required"
        }
    )
    submit = SubmitField(
        label='登录',
        render_kw={
            "class": "btn btn-lg btn-success btn-block"
        }
    )

    def validate_name(self, field):
        name = field.data
        user = User.query.filter_by(name=name).count()
        if user == 0:
            raise ValidationError("帐号不存在！")


class UserdetailForm(FlaskForm):
    """会员详情表单"""
    name = StringField(
        label='昵称',
        validators=[
            DataRequired("请输入昵称！")
        ],
        description="昵称",
        render_kw={
            "class": "form-control",
            "id": "input_name",
            "placeholder": "请输入昵称！"
        },
    )
    email = StringField(
        label='邮箱',
        validators=[
            DataRequired("请输入邮箱！"),
            email("邮箱格式不正确!")
        ],
        description="邮箱",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入邮箱！",
            # "required": "required"
        },
    )
    phone = StringField(
        label='手机号',
        validators=[
            DataRequired("请输入手机号！"),
            Regexp("^1[3458]\d{9}$", message="手机号格式错误")
        ],
        description="手机号",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入手机号！",
            # "required": "required"
        },
    )

    info = TextAreaField(
        label='个性签名',
        validators=[
            DataRequired("请输入个性签名！")
        ],
        description="个性签名",
        render_kw={
            "class": "form-control",
            "rows":"10"
        },
    )
    face = FileField(
        label='头像',
        validators=[
            DataRequired("请上传头像！")
        ],
        description="头像",
        render_kw={
            "id": "input_face",
        },
    )

    submit = SubmitField(
        label='保存修改',
        render_kw={
            "class": "btn btn-success"
        }
    )


class PwdForm(FlaskForm):
    """会员密码表单"""
    pwd = PasswordField(
        label='旧密码',
        validators=[
            DataRequired("请输入旧密密码")
        ],
        description="旧密码",
        render_kw={
        "class" : "form-control",
        "placeholder" : "请输入旧密码!",
        # "required" : "required"
        }
    )
    new_pwd =  PasswordField(
        label='新密码',
        validators=[
            DataRequired("请输入新密码！"),
        ],
        description="密码",
        render_kw={
        "class" : "form-control",
        "placeholder" : "请输入新密码！",
        # "required" : "required"
        }
    )
    submit = SubmitField(
        label='修改密码',
        render_kw={
    "class" : "btn btn-success"
        }
    )
    def validate_pwd(self, field):
        pwd = field.data
        name = session["user"]
        user = User.query.filter_by(name=name).first()
        if not user.check_pwd(pwd):
            raise ValidationError("旧密码错误！请重新输入")

class CommentForm(FlaskForm):
    """评论表单"""
    content = TextAreaField(
        label='内容',
        validators=[
            DataRequired("请输入评论内容！")
        ],
        description="内容",
        render_kw={
            "id": "input_content",
        },
    )
    submit = SubmitField(
        label='提交评论',
        render_kw={
            "class": "btn btn-success",
            "id" : "btn-sub"
        }
    )

