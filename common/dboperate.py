# coding: gbk
from sqlalchemy import Column, Integer, String, DateTime, func
from sqlalchemy import Boolean, TIMESTAMP, UniqueConstraint, ForeignKey  # 最后跟关系相关
from main import db


# 获得数据库会话连接
def get_session():
    return db.session


# 博客表
class Blogs(db.Model):
    __tablename__ = 'blogs'
    id = Column(Integer, nullable=True, primary_key=True, autoincrement=True)
    user_id = Column(Integer, nullable=True, default=1)
    username = Column(String(255), nullable=True)
    content = Column(String(255), nullable=True)
    time = Column(DateTime, default=func.now())  # 不更新，就是发表时间
    likes = Column(Integer, nullable=True, default=0)
    comment = Column(Integer, nullable=True, default=0)
    picture = Column(String(255))


# 信息表
class Messages(db.Model):
    __tablename__ = 'messages'
    id = Column(Integer, nullable=True, primary_key=True, autoincrement=True)
    userid = Column(Integer, nullable=True)
    username=Column(String(255), nullable=True)
    blogid = Column(Integer, nullable=True)


# 关注表
class Followers(db.Model):
    __tablename__ = 'followers'
    id = Column(Integer, nullable=True, primary_key=True, autoincrement=True)
    userid = Column(Integer, nullable=True)
    follower_id = Column(Integer, nullable=True)
    follower_name = Column(String(255), nullable=True)


# 评论表
class Comments(db.Model):
    __tablename__ = 'comments'
    id = Column(Integer, nullable=True, primary_key=True, autoincrement=True)
    userid = Column(Integer, nullable=True)
    username = Column(String(255), nullable=True)
    blogid = Column(Integer, nullable=True)
    content = Column(String(255), nullable=True)
    time = Column(DateTime, default=func.now(), onupdate=func.now())


# 点赞表
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
# 删所有表
# db.drop_all()
# 建所有表
# db.create_all()
