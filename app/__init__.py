# -*- encoding=utf-8 -*-
from flask import Flask
from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
import os


app = Flask(__name__)
# 将配置文件引入
app.config.from_pyfile('app.conf')
app.config['UP_DIR'] = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'static/uploads/')
app.config['FC_DIR'] = os.path.join(os.path.abspath(os.path.dirname(__file__)), "static/users/")

db = SQLAlchemy(app)

# 引入前台蓝图
from app.home_routes.index import main as index_routes
from app.home_routes.user import main as user_routes

# 引入后台蓝图
from app.admin_routes.index import main as admin_routes
from app.admin_routes.tag import main as tag_routes
from app.admin_routes.movie import main as movie_routes
from app.admin_routes.preview import main as preview_routes
from app.admin_routes.user import main as admin_user_routes
from app.admin_routes.comment import main as comment_routes
from app.admin_routes.moviecol import main as moviecol_routes
from app.admin_routes.log import main as log_routes
from app.admin_routes.role import main as role_routes
from app.admin_routes.admin import main as administrator_routes
from app.admin_routes.auth import main as auth_routes


# 注册蓝图
app.register_blueprint(index_routes)
app.register_blueprint(user_routes, url_prefix='/user')

app.register_blueprint(admin_routes, url_prefix='/admin')
app.register_blueprint(tag_routes, url_prefix='/admin/tag')
app.register_blueprint(movie_routes, url_prefix='/admin/movie')
app.register_blueprint(preview_routes, url_prefix='/admin/preview')
app.register_blueprint(admin_user_routes, url_prefix='/admin/user')
app.register_blueprint(comment_routes, url_prefix='/admin/comment')
app.register_blueprint(moviecol_routes, url_prefix='/admin/moviecol')
app.register_blueprint(log_routes, url_prefix='/admin/log')
app.register_blueprint(role_routes, url_prefix='/admin/role')
app.register_blueprint(auth_routes, url_prefix='/admin/auth')
app.register_blueprint(administrator_routes, url_prefix='/admin/administrator')


@app.errorhandler(404)
def page_not_found(error):
    return render_template("home/404.html"), 404

