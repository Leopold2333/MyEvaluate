from common.dboperate import Users
from common.dboperate import get_session
from flask import session

dbsession = get_session()


# 封装用户类的操作
class OpUsers:
    def commit(self):
        dbsession.commit()
        dbsession.close()

    # 增加一个注册用户类
    def insert(self, username, email, phone, password, intro):
        user = Users(username=username, email=email, phone=phone, password=password, intro=intro)
        dbsession.add(user)
        self.commit()

    # 得到用户数量
    def get_count(self):
        return dbsession.query(Users).count()

    # 按用户名查找
    def find_by_username(self, username):
        return dbsession.query(Users).filter(Users.username == username).first()

    def find_users_by_ids(self, userid):
        row = dbsession.query(Users).filter(Users.id.in_(userid)).all()
        return row

    # 改变状态
    def change_state(self, ret, state):
        ret.state = state
        ret.n_wrong = 0
        self.commit()

    # 用户退出
    def exit(self, username):
        ret = self.find_by_username(username)
        self.change_state(ret, 'valid')

    # 通过邮箱重置密码
    def reset_pwd_by_email(self, email, password):
        ret = dbsession.query(Users).filter(Users.email == email).first()
        ret.password = password
        self.commit()

    # 检查登录状态
    def check_state(self):
        ret = dbsession.query(Users).all()
        for row in ret:
            if row.state == "login":
                session["userid"] = row.id
                session["username"] = row.username
                session["userpic"] = 0
                return row.id
        return ""