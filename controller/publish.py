from flask import Blueprint, request, jsonify, session
from dao.blogs import OpBlogs
from dao.messages import OpMessages
import main

publish = Blueprint('publish', __name__)


@publish.route('/publish', methods=['POST'])
def set_publish():
    # 发布博文的文本信息
    content = request.form.get('content')
    user_id = session.get('userid')
    username = session.get('username')
    # 图片们的url序列获取
    dest_list = main.parse_image(request.form.get('html'))
    picture = ""
    for item in dest_list:
        if picture == "" and item is not None:
            picture = item
        else:
            picture += " " + item
    if len(content) == 0 and len(dest_list) == 0:
        return jsonify({'errmsg': '什么都木有写呀！'})
    try:
        blogid=OpBlogs().insert(user_id, username, content, 0, 0, picture)
        aiteId = request.form.get('aite').split(' ')
        print(aiteId)
        if len(aiteId)>0 and aiteId[0]!='':
            mess=OpMessages()
            print(mess)
            mess.insert_n(blogid, [int(b) for b in aiteId])
        return jsonify({'errmsg': '博文发表成功'})
    except:
        return jsonify({'errmsg': '博文发表失败'})


@publish.route('/delete', methods=['POST'])
def set_delete():
    blogid = request.form.get('blogid')
    OpBlogs().delete_by_blogid(blogid)
    return jsonify({'errmsg': '博文删除成功'})
