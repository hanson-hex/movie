# -*- encoding=utf-8 -*-
from flask import session
from flask import redirect
from flask import request
from flask import url_for
from functools import wraps
from app.models.admin import Admin
from app.models.role import Role
from app.models.auth import Auth
from flask import abort
from app.utils import log

def admin_login_req(f):
    """
    权限登录装饰器
    """
    @wraps(f)
    def decorator(*args, **kwargs):
        if 'admin' not in session:
            return redirect(url_for('admin.login', next=request.url))
        return f(*args, **kwargs)
    return decorator

def admin_auth(f):
    """权限访问装饰器"""
    @wraps(f)
    def decorator(*args, **kwargs):
        admin = Admin.query.join(Role).filter(
            Admin.id == session['admin_id'],
            Role.id ==Admin.role_id,
        ).first()
        auths = admin.role.auths
        print('auths', auths)
        auths = list(map(lambda v : int(v), auths.split(',')))
        auths_url = Auth.query.all()
        print('auths_url', auths_url)
        urls = [v.url for v in auths_url for i in auths if v.id == i]
        print('urls', urls)
        url = request.url_rule
        print('url', url)
        if str(url) not in urls:
            abort(404)
        return f(*args, **kwargs)
    return decorator


