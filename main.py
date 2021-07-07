# coding: gbk
from flask import Flask, session
from flask_sqlalchemy import SQLAlchemy
import pymysql
import time
import json
import os
import re

pymysql.install_as_MySQLdb()
app = Flask(__name__, template_folder='templates', static_url_path='/', static_folder='static')
app.config.from_pyfile('config.py', silent=True)
db = SQLAlchemy(app)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')


# ΢��ϵͳ����������Զ���ʼ��ueditor����
@app.route('/ueditor/', methods=['GET', 'POST'])
def ueditor():
    # ��Ӧ����
    mime_type = 'application/json'
    # �������صĽ��
    result = {}
    # �����ļ�·��Ϊ��MyEvaluate/static/ueditor/jsp/config.json��
    config_file = os.path.join(app.static_folder, 'ueditor', 'jsp', 'config.json')
    # ���ڴ�������ļ�������
    CONFIG = {}
    # ��ȡ�����ļ�����ʽ��
    with open(config_file, 'r', encoding='utf8') as f:
        try:
            # ȥ�������ļ��е�ע�Ͳ���jsonתΪpython�е��ֵ�
            CONFIG = json.loads(re.sub(r'\/\*.*\*\/', '', f.read()))
        except:
            CONFIG = {}

    # �ж��û�����
    action = request.args.get('action')
    print(action)
    # ���ڱ����ϴ�����������
    config = {}
    # �ύ��ͼƬ������
    field_name = ''
    # �����ҳ���ʼ�����ȡ����CONFIG
    if action == 'config':
        result = CONFIG
    # ������ϴ�ͼƬ
    elif action == 'uploadimage':
        # ͨ����ǰ�����û�����һ�������ͼƬ������
        who = session.get("username") + str(session.get("userpic")) + ".png"
        # �û��ϴ���ͼƬ�ݴ��ڡ�/MyEvaluate/static/ueditor/jsp/upload/image/����
        filename = os.path.join(app.static_folder, 'ueditor', 'jsp', 'upload', 'image', who).replace("\\", "/")
        upfile = request.files['upfile']
        upfile.save(filename)
        compress(filename, filename, 600)
        result = {
            "state": "SUCCESS",
            "url": "/ueditor/jsp/upload/image/" + who,
            "title": who,
            "original": who
        }
        session['userpic'] = session.get('userpic') + 1
    else:
        result['state'] = '�����ַ����'
    return jsonify(result)


# ѹ��ͼƬ������������������
def compress(filename, destname, width):
    from PIL import Image
    im = Image.open(filename)
    x, y = im.size
    if x > width:
        ynew = int(y * width / x)
        xnew = width
        temp = im.resize((xnew, ynew), Image.ANTIALIAS)
        os.remove(filename)
        temp.save(destname, quality=80)
    else:
        im.save(destname, quality=80)


# ��ȡ��������ͼƬ
def parse_image(content):
    import re
    i = 0
    temp_list = re.findall('<img src="(.+?)"', content)
    dest_list = []
    for url in temp_list:
        now = str(time.strftime('IMG_%Y%m%d_%H%M%S')) + str(i) + ".png"
        who = session.get("username") + str(i) + ".png"
        filename = os.path.join(app.static_folder, 'ueditor', 'jsp', 'upload', 'image', who).replace("\\", "/")
        destname = os.path.join(app.static_folder, 'compress', now).replace("\\", "/")
        if "http" in url:
            get_image(url, filename)
        compress(filename, destname, 400)
        dest_list.append(now)
        i += 1
    return dest_list


# Զ������ͼƬ����
def get_image(url, filename):
    import requests
    response = requests.get(url)
    with open(file=filename, mode="wb") as file:
        file.write(response.content)


if __name__ == '__main__':
    # ��ͼ��ע�ᣬ����ģ���������db����controller��Ҳ������db��main���Ե�����controller����ֹѭ��
    # ��ͼ��ע�ᣬ����ģ���������db����controller��Ҳ������db��main���Ե�����controller����ֹѭ��
    from controller.index import *

    app.register_blueprint(index)

    from controller.LoginController import *

    app.register_blueprint(login)

    from controller.RegisterController import *

    app.register_blueprint(register)

    app.run(debug=True)
