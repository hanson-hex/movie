# -*- encoding=utf-8 -*-
from flask import session
from flask import redirect
from flask import request
from flask import url_for
from functools import wraps

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