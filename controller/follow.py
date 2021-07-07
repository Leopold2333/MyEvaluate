from flask import Blueprint, session, request, jsonify
from dao.followers import OpFollowers

follow = Blueprint('follow', __name__)


@follow.route('/follow/yes', methods=['POST'])
def addFollow():
    userid = session.get("userid")
    follower_id = request.form.get('followedB')
    follower_name = request.form.get('B_name')
    username = session.get("username")
    if username is None:
        return jsonify({"errmsg": "关注失败，请检查登录状态"})
    else:
        if username == follower_name:
            return jsonify({"errmsg": "做伪主不要太自恋！"})
        else:
            follw=OpFollowers()
            follw.insert(userid, follower_id, follower_name)

            Aite = follw.find_AllFollows_by_userid(userid)
            AiteRe = []
            for item in Aite:
                dd = {}
                dd['followedB'] = item.follower_id
                dd['B_name'] = item.follower_name
                AiteRe.append(dd)
            return jsonify({"errmsg": "关注成功！", "AiteRe": AiteRe})


@follow.route('/follow/no', methods=['POST'])
@follow.route('/page/follow/no', methods=['POST'])
def cancelFollow():
    userid = session.get("userid")
    follower_id = request.form.get('followedB')
    who = session.get("username")
    if who is None:
        return jsonify({"errmsg": "取消失败，请检查登录状态"})
    else:
        follw = OpFollowers()
        follw.delete_by_id_follower(userid, follower_id)
        Aite = follw.find_AllFollows_by_userid(userid)
        AiteRe = []
        for item in Aite:
            dd = {}
            dd['followedB'] = item.follower_id
            dd['B_name'] = item.follower_name
            AiteRe.append(dd)
        return jsonify({"errmsg": "取消成功！","AiteRe":AiteRe})
