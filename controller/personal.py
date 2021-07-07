from flask import Blueprint, render_template, request, session
from dao.users import OpUsers

personal = Blueprint('personal', __name__)


@personal.route('/personal', methods=['GET', 'POST'])
def person_page():
    username = request.values.get("user")
    # 获取该用户全部信息
    result = OpUsers().find_by_username(username)
    return render_template('Personal.html', result=result, login=session.get('username'))
