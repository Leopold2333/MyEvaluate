from flask import Blueprint, request, session, jsonify
from dao.blogs import OpBlogs
from dao.comments import OpComments

comment = Blueprint('comment', __name__)


@comment.route('/comment', methods=['POST'])
def addComment():
    username = session.get('username')
    if username is None:
        return jsonify({'errmsg': '发表失败，请检查登陆状态'})
    else:
        # 指定博文增加评论
        blogid = request.form.get('blogid')
        content = request.form.get('content').strip()
        OpComments().insert(blogid, username, content)
        OpBlogs().add_comment(blogid)
        return jsonify({'errmsg': '评论发表成功'})


@comment.route('/Commentinfo', methods=['POST'])
def queryComment():
    blogid = request.form.get('blogid')
    rows = OpComments().find_by_blogid(blogid)
    result = []
    for items in rows:
        res = {'username': items.username, 'time': items.time, 'content': items.content}
        result.append(res)
    return jsonify({'msg': result})
