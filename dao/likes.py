from common.dboperate import Likes
from common.dboperate import get_session

dbsession = get_session()


# 封装点赞类的操作
class OpLikes:
    def commit(self):
        dbsession.commit()
        dbsession.close()

    # 增加一个新点赞
    def insert(self, blogid, userid, username):
        likes = Likes(blogid=blogid, userid=userid, username=username)
        dbsession.add(likes)
        self.commit()

    # 根据博客id全删除
    def delete_by_blogid(self, blogid):
        likes = dbsession.query(Likes).filter(Likes.blogid == blogid).all()
        [dbsession.delete(i) for i in likes]
        self.commit()

    # 根据博客id和用户id精准删除
    def delete_by_blogid_userid(self, blogid, userid):
        dbsession.query(Likes).filter(Likes.blogid == blogid and Likes.userid == userid).delete()
        self.commit()

    # 得到点赞数量
    def get_count(self):
        return dbsession.query(Likes).count()

    # 按博客id查找点赞列表
    def find_by_blogid(self, blogid):
        return dbsession.query(Likes).order_by(Likes.blogid.desc()).filter(Likes.blogid == blogid).all()

    # 按博客id列表查找点赞列表
    def find_by_blogids(self, result1):
        row = dbsession.query(Likes).order_by(Likes.blogid.desc()).filter(Likes.blogid == result1[0].id).all()
        for i in range(1, len(result1)):
            row += dbsession.query(Likes).order_by(Likes.blogid.desc()).filter(Likes.blogid == result1[i].id).all()
        return row

    def find_usernames_by_blogid(self, blogid):
        row = dbsession.query(Likes).filter(Likes.blogid == blogid).all()
        re = []
        for i in row:
            re.append(i.username)
        return ','.join(re)

    def find_blogids_by_userid(self, userid):
        row = dbsession.query(Likes).filter(Likes.userid == userid).all()
        re = []
        for i in row:
            re.append(i.blogid)
        return re
