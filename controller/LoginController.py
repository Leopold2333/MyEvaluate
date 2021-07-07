from flask import Blueprint, request, jsonify, session
from common.times import count_time
from dao.Student import OpStudent
from dao.Teacher import OpTeacher

login = Blueprint('login', __name__)


def check_pwd(user, ret, userId, password, type):
    if ret.password == password:
        session['userid'] = userId
        if type == 'student':
            session['username'] = ret.username
        else:
            session['username'] = ret.name
        return "登陆成功!"
    else:
        return "密码错误!"


# 执行登录请求
@login.route('/login', methods=['POST'])
def set_login():
    Id = request.form.get('userId')
    type = request.form.get('type')
    if type == 'student':
        user = OpStudent()
    else:
        user = OpTeacher()
    ret = user.find_users_by_ids(Id)
    if ret is None:
        return jsonify({"errmsg": "用户不存在，请先注册"})
    else:
        password = request.form.get('password')
        text = check_pwd(user, ret, Id, password, type)
        return jsonify({"errmsg": text})


@login.route('/exit', methods=['POST'])
def set_exit():
    session.pop('userid')
    session.pop('username')
    session['state'] = 'all'
    return jsonify({"errmsg": "退出成功"})
