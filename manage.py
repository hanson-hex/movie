# -*- encoding=utf-8 -*-

from app import app
from app import db
from flask_script import Manager
from app.models.user import User
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



from app.utils import log

manager = Manager(app)


def create_admin():
    """
    创建管理员
    """
    log('程序执行创建添加管理员')
    for i in range(1, 10):
        n = str(i)
        form = dict(
            name='admin'+str(i),
            pwd=n.zfill(3),
            role_id = 1
        )
        admin = Admin(form)
        log('a', admin)
        admin.save()

def create_role():
    """
    创建角色
    """
    form1 = dict(
        name="普通管理员",
        auths=""
    )
    form2 = dict(
        name="超级管理员",
        auths=""
    )
    role1 = Role(form1)
    role2 = Role(form2)
    role1.save()
    role2.save()


@manager.command
def init_database():

    # 清空数据表
    db.drop_all()
    # log('清空数据表')
    # 新建数据表
    # log('新建数据表')
    db.create_all()
    create_role()
    create_admin()




if __name__ == '__main__':
    manager.run()
