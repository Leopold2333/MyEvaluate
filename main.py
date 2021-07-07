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


# 微博系统加载最初会自动初始化ueditor配置
@app.route('/ueditor/', methods=['GET', 'POST'])
def ueditor():
    # 响应类型
    mime_type = 'application/json'
    # 用来返回的结果
    result = {}
    # 配置文件路径为“MyEvaluate/static/ueditor/jsp/config.json”
    config_file = os.path.join(app.static_folder, 'ueditor', 'jsp', 'config.json')
    # 用于存放配置文件的内容
    CONFIG = {}
    # 读取配置文件并格式化
    with open(config_file, 'r', encoding='utf8') as f:
        try:
            # 去除配置文件中的注释并将json转为python中的字典
            CONFIG = json.loads(re.sub(r'\/\*.*\*\/', '', f.read()))
        except:
            CONFIG = {}

    # 判断用户动作
    action = request.args.get('action')
    print(action)
    # 用于保存上传操作的配置
    config = {}
    # 提交的图片表单名称
    field_name = ''
    # 如果是页面初始化则读取配置CONFIG
    if action == 'config':
        result = CONFIG
    # 如果是上传图片
    elif action == 'uploadimage':
        # 通过当前在线用户生成一个有序的图片序列名
        who = session.get("username") + str(session.get("userpic")) + ".png"
        # 用户上传的图片暂存在“/MyEvaluate/static/ueditor/jsp/upload/image/”中
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
        result['state'] = '请求地址出错'
    return jsonify(result)


# 压缩图片操作，避免容量过大
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


# 获取博文所有图片
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


# 远程下载图片保存
def get_image(url, filename):
    import requests
    response = requests.get(url)
    with open(file=filename, mode="wb") as file:
        file.write(response.content)


if __name__ == '__main__':
    # 蓝图的注册，由于模型里调用了db，而controller里也引用了db，main里仍调用了controller，防止循环
    # 蓝图的注册，由于模型里调用了db，而controller里也引用了db，main里仍调用了controller，防止循环
    from controller.index import *

    app.register_blueprint(index)

    from controller.LoginController import *

    app.register_blueprint(login)

    from controller.RegisterController import *

    app.register_blueprint(register)

    app.run(debug=True)
