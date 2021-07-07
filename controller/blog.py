from dao.blogs import OpBlogs
from flask import Blueprint, jsonify, session

blog = Blueprint('blog', __name__)


# 作为controller，截获/user，并实例化一个类，将指定的信息返回回视图
@blog.route('/blog')
def blog_demo():
    blogs = OpBlogs()
    if 'userid'not in session:
        row = blogs.find_n_from_offset(0, 5, 0)
    else:
        row = blogs.find_n_from_offset(0, 5, session['userid'])
    # 将list转为json传给前端
    return jsonify(model_list(row))


def model_list(row):
    lt = []
    for item in row:
        dic = {}
        for k, v in item.__dict__.items():
            if not k.startswith('_sa_instance_state'):
                dic[k] = v
        lt.append(dic)
    return lt
