import os

# 设置安全锁
SECRET_KEY = os.urandom(24)
# ��������α�챣��
# CSRF_ENABLED = True

# ���ݿ�����
pwd = 'root'
db_name = 'blogs'
SQLALCHEMY_DATABASE_URI = f'mysql://root:{pwd}@localhost:3306/{db_name}?charset=utf8'
SQLALCHEMY_TRACK_MODIFICATIONS = False
