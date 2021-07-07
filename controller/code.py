from flask import Blueprint, session, request, jsonify, render_template
from dao.users import OpUsers
from common.emails import send_email, generate_ecode
# from common.verify import ImageCode

code = Blueprint('code', __name__)

# 触发发送邮件
@code.route('/ecode', methods=['POST'])
def ecode():
    receiver = request.form.get('receiver')
    session['email'] = receiver
    text = send_email(receiver)
    return jsonify({'errmsg': text})
# 将页面重置为密码修改的页面
@code.route('/reset')
def reset():
    return render_template('reset.html')
# 获取密码，重置密码
@code.route('/verify', methods=['POST'])
def judge():
    try:
        OpUsers().reset_pwd_by_email(session.get('email'), request.form.get('password'))
        session.pop('email')
        return jsonify({'errmsg': '重置成功'})
    except:
        return jsonify({'errmsg': '重置失败'})
