from common.dboperate import Followers
from common.dboperate import get_session

dbsession = get_session()


# ��װ��ע����Ĳ���
class OpFollowers:
    def commit(self):
        dbsession.commit()
        dbsession.close()

    def insert(self, userid, follower_id, follower_name):
        follower = Followers(userid=userid, follower_id=follower_id, follower_name=follower_name)
        dbsession.add(follower)
        self.commit()

    def delete_by_id_follower(self, _id, follower):
        dbsession.query(Followers).filter(Followers.userid == _id , Followers.follower_id == follower).delete()
        self.commit()

    # ��id����
    def find_by_userids(self, userids):
        row = dbsession.query(Followers).filter(Followers.userid == userids).all()
        re = []
        for i in row:
            re.append(i.follower_id)
        return re

    def find_AllFollows_by_userid(self, userid):
        print('find_AllFollows_by_userid',userid)
        return dbsession.query(Followers).filter(Followers.userid==userid).all()