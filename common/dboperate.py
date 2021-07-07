# coding: gbk
from sqlalchemy import Column, Integer, String, DateTime, func
from sqlalchemy import Boolean, TIMESTAMP, UniqueConstraint, ForeignKey  # ������ϵ���
from main import db


# ������ݿ�Ự����
def get_session():
    return db.session


# ���ͱ�
class Blogs(db.Model):
    __tablename__ = 'blogs'
    id = Column(Integer, nullable=True, primary_key=True, autoincrement=True)
    user_id = Column(Integer, nullable=True, default=1)
    username = Column(String(255), nullable=True)
    content = Column(String(255), nullable=True)
    time = Column(DateTime, default=func.now())  # �����£����Ƿ���ʱ��
    likes = Column(Integer, nullable=True, default=0)
    comment = Column(Integer, nullable=True, default=0)
    picture = Column(String(255))


# ��Ϣ��
class Messages(db.Model):
    __tablename__ = 'messages'
    id = Column(Integer, nullable=True, primary_key=True, autoincrement=True)
    userid = Column(Integer, nullable=True)
    username=Column(String(255), nullable=True)
    blogid = Column(Integer, nullable=True)


# ��ע��
class Followers(db.Model):
    __tablename__ = 'followers'
    id = Column(Integer, nullable=True, primary_key=True, autoincrement=True)
    userid = Column(Integer, nullable=True)
    follower_id = Column(Integer, nullable=True)
    follower_name = Column(String(255), nullable=True)


# ���۱�
class Comments(db.Model):
    __tablename__ = 'comments'
    id = Column(Integer, nullable=True, primary_key=True, autoincrement=True)
    userid = Column(Integer, nullable=True)
    username = Column(String(255), nullable=True)
    blogid = Column(Integer, nullable=True)
    content = Column(String(255), nullable=True)
    time = Column(DateTime, default=func.now(), onupdate=func.now())


# ���ޱ�
class Likes(db.Model):
    __tablename__ = 'likes'
    id = Column(Integer, nullable=True, primary_key=True, autoincrement=True)
    blogid = Column(Integer, nullable=True)
    userid = Column(Integer, nullable=True)
    username = Column(String(255), nullable=True)


class Student(db.Model):
    __tablename__ = 'student'
    id = Column(Integer, nullable=True, primary_key=True, autoincrement=True)
    username = Column(String(31), nullable=True, unique=True)
    password = Column(String(31), nullable=True)
    sex = Column(String(31), nullable=True)
    grade = Column(Integer, nullable=True)
    department = Column(String(31), nullable=True)
    major = Column(String(31), nullable=True)
    phone = Column(String(15), nullable=True)
    ad_date = Column(DateTime, default=func.now(), onupdate=func.now())


class Teacher(db.Model):
    __tablename__ = 'teacher'
    id = Column(Integer, nullable=True, primary_key=True, autoincrement=True)
    password = Column(String(31), nullable=True)
    name = Column(String(31), nullable=True, unique=True)
    sex = Column(String(31), nullable=True)
    research_direction = Column(String(31), nullable=True)
    title = Column(String(31), nullable=True)
    email = Column(String(31), nullable=True)
    phone = Column(String(15), nullable=True)
    achievement = Column(String(31), nullable=True)
    # department = Column(String(31), nullable=True)
# ɾ���б�
# db.drop_all()
# �����б�
# db.create_all()
