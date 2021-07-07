from common.dboperate import Student
from common.dboperate import get_session
from flask import session

dbsession = get_session()


# 封装学生类的操作
class OpStudent:
    def commit(self):
        dbsession.commit()
        dbsession.close()

    # 增加一个注册用户类
    def insert(self, username, password, sex, grade, department, major, phone):
        user = Student(username=username, password=password, sex=sex, grade=grade, department=department,
                       major=major, phone=phone)
        dbsession.add(user)
        self.commit()

    # 得到学生数量
    def get_count(self):
        return dbsession.query(Student).count()

    # 按用户名查找
    def find_by_username(self, username):
        return dbsession.query(Student).filter(Student.username == username).first()

    # 按学号查找
    def find_users_by_ids(self, Id):
        row = dbsession.query(Student).filter(Student.id.in_(Id)).all()
        return row
