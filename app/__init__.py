# -*- encoding=utf-8 -*-
from flask import Flask
from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# 将配置文件引入
app.config.from_pyfile('app.conf')


db = SQLAlchemy(app)

# 引入前台蓝图
from app.home_routes.index import main as index_routes
from app.home_routes.user import main as user_routes

# 引入后台蓝图
from app.admin_routes.index import main as admin_routes
from app.admin_routes.index import main as tag_routes


# 注册蓝图
app.register_blueprint(index_routes)
app.register_blueprint(user_routes, url_prefix='/user')

app.register_blueprint(admin_routes, url_prefix='/admin')
app.register_blueprint(tag_routes, url_prefix='/tag')



@app.errorhandler(404)
def page_not_found(error):
    return render_template("home/404.html"), 404

