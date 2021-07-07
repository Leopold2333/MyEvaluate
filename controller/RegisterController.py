from flask import Blueprint, request, jsonify, session
from common.times import count_time
from dao.Student import OpStudent
from dao.Teacher import OpTeacher

register = Blueprint('register', __name__)


@register.route('/register', methods=['POST'])
def addUser():
    userType = request.form.get('type')
    username = request.form.get('username')
    password = request.form.get('password')
    sex = request.form.get('sex')
    phone = request.form.get('phone')
    # 创建各个键值对应的值
    if userType == 'student':
        grade = request.form.get('grade')
        department = request.form.get('department')
        major = request.form.get('major')
        try:
            OpStudent().insert(username, password, sex, grade, department, major, phone)
            return {'errmsg': '学生注册成功'}
        except:
            return {'errmsg': '学生注册失败'}
    else:
        researchDirection = request.form.get('researchDirection')
        title = request.form.get('title')
        email = request.form.get('email')
        achievement = request.form.get('achievement')
        try:
            OpTeacher().insert(username, password, sex, researchDirection, title, email, phone)
            return {'errmsg': '教师注册成功'}
        except:
            return {'errmsg': '教师注册失败'}
