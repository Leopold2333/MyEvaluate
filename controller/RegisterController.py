from flask import Blueprint, request, jsonify, session
from common.times import count_time
from dao.Student import OpStudent
from dao.Teacher import OpTeacher

register = Blueprint('register', __name__)


@register.route('/register', methods=['POST'])
def addUser():
    userType = request.form.get('type')
    username = request.form.get('username')
    code = request.form.get('code')
    password = request.form.get('password')
    sex = request.form.get('sex')
    print(sex)
    if sex == 1:
        sex = "男"
    else:
        sex = "女"
    phone = request.form.get('phone')
    # 创建各个键值对应的值
    if userType == 'student':
        grade = request.form.get('grade')
        if grade == 1:
            grade = "大一"
        elif grade == 2:
            grade = "大二"
        elif grade == 3:
            grade = "大三"
        elif grade == 4:
            grade = "大四"
        department = request.form.get('department')
        major = request.form.get('major')
        adDate = request.form.get('adDate')
        try:
            OpStudent().insert(username, code, password, sex, grade, department, major, phone, adDate)
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
