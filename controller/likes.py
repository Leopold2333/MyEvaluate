from flask import Blueprint, request, session, jsonify
from dao.blogs import OpBlogs
from dao.likes import OpLikes

likes = Blueprint('likes', __name__)

@likes.route('/page/likes/yes', methods=['POST'])
@likes.route('/likes/yes', methods=['POST'])
def add():
    if session.get('username') is None:
        return jsonify({'errmsg': '点赞失败，请检查登陆状态'})
    else:
        # 如何指定博文增加评论
        _blogid = request.form.get('blogid')
        _blogs = OpBlogs()
        _likes = OpLikes()
        _userid = session.get('userid')
        _username = session.get('username')
        # 判断这个是不是自己
        row = _blogs.find_by_id(_blogid)
        if _username == row.username:
            return jsonify({'errmsg': '做人不能太自恋'})
        else:
            rows = _likes.find_by_blogid(_blogid)
            for row in rows:
                if row.username == _username:
                    return jsonify({'errmsg': '你已经点过赞啦，小兄弟'})
            _blogs.add_likes(_blogid)
            _likes.insert(_blogid, _userid, _username)
            return jsonify({'errmsg': '点赞成功'})

@likes.route('/page/likes/no', methods=['POST'])
@likes.route('/likes/no', methods=['POST'])
def cancel():
    if session.get('username') is None:
        return jsonify({'errmsg': '请检查登陆状态'})
    else:
        blogid = request.form.get('blogid')
        userid = session.get('userid')
        OpLikes().delete_by_blogid_userid(blogid, userid)
        OpBlogs().delete_likes(blogid)
        return jsonify({'errmsg': '取消成功'})


@likes.route('/likeinfo', methods=['POST'])
def getinfo():
    blogid = request.form.get('blogid')
    try:
        row = OpLikes().find_usernames_by_blogid(blogid)
    except:
        return jsonify({'errmsg': '服务端出错'})
    return jsonify({'errmsg': row})
