import os

# 设置安全锁
SECRET_KEY = os.urandom(24)
#
# CSRF_ENABLED = True

# 连接数据库evaluate
pwd = 'root'
db_name = 'evaluate'
SQLALCHEMY_DATABASE_URI = f'mysql://root:{pwd}@localhost:3306/{db_name}?charset=utf8'
SQLALCHEMY_TRACK_MODIFICATIONS = False
