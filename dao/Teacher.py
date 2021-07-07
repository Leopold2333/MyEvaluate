from common.dboperate import Teacher
from common.dboperate import get_session
from flask import session

dbsession = get_session()


# 封装学生类的操作
class OpTeacher:
    def commit(self):
        dbsession.commit()
        dbsession.close()

    # 增加一个注册用户类
    def insert(self, name, password, sex, researchDirection, title, email, phone):
        user = Teacher(name=name, password=password, sex=sex, research_direction=researchDirection, title=title,
                       email=email, phone=phone)
        dbsession.add(user)
        self.commit()

    # 得到学生数量
    def get_count(self):
        return dbsession.query(Teacher).count()

    # 按工号查找
    def find_users_by_ids(self, Id):
        row = dbsession.query(Teacher).filter(Teacher.id.in_(Id)).all()
        return row
