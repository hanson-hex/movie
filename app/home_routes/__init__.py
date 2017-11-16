from functools import wraps
from flask import session
from flask import redirect
from flask import url_for


# 登录装饰器
def user_login_req(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        if "user" not in session:
            return redirect(url_for("index.login"))
        return f(*args, **kwargs)
    return decorator