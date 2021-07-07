from flask import session
from sqlalchemy import func
from common.dboperate import Blogs, Comments, Likes, Messages
from common.dboperate import get_session
from dao.likes import OpLikes
from dao.messages import OpMessages
from dao.followers import OpFollowers

dbsession = get_session()


class OpBlogs:
    def commit(self):
        dbsession.commit()

    def insert(self, user_id, username, content, likes, comment, picture):
        time = func.now()
        blog = Blogs(user_id=user_id, username=username, content=content, likes=likes, comment=comment, picture=picture,
                     time=time)
        dbsession.add(blog)
        self.commit()
        # 需要获得新发布博客的id
        newblog = dbsession.query(Blogs).filter(Blogs.time == time).first()
        return newblog.id

    # 删除博客
    def delete_by_blogid(self, blogid):
        dbsession.query(Blogs).filter(Blogs.id == blogid).delete()
        # 删评论、点赞和消息列表
        comments = dbsession.query(Comments).filter(Comments.blogid == blogid).all()
        [dbsession.delete(i) for i in comments]
        likes = dbsession.query(Likes).filter(Likes.blogid == blogid).all()
        [dbsession.delete(i) for i in likes]
        messages = dbsession.query(Messages).filter(Messages.blogid == blogid).all()
        [dbsession.delete(i) for i in messages]
        # OpComments.delete_by_blogid(blogid)
        # OpLikes.delete_by_blogid(blogid)
        # OpMessages.delete_by_blogid(blogid)
        self.commit()

    def delete_likes(self, blogid):
        row = dbsession.query(Blogs).filter(Blogs.id == blogid).first()
        row.likes -= 1
        self.commit()

    def get_count(self):
        return dbsession.query(Blogs).count()

    def get_all(self):
        return dbsession.query(Blogs).all()

    def add_comment(self, blogid):
        row = dbsession.query(Blogs).filter(Blogs.id == blogid).first()
        row.comment += 1
        self.commit()

    def add_likes(self, blogid):
        row = dbsession.query(Blogs).filter(Blogs.id == blogid).first()
        row.likes += 1
        self.commit()

    def find_by_id(self, _id):
        return dbsession.query(Blogs).filter(Blogs.id == _id).first()

    # 从offset起得到n个
    def find_n_from_offset(self, start, count, userid):
        global result1
        rank = session.get('rank')
        state = session.get('state')
        if state == 'all':
            if rank == 'time':
                # 按照时间顺序挑5个
                result1 = dbsession.query(Blogs).order_by(Blogs.time.desc()).limit(count).offset(start).all()
            elif rank == 'comment':
                result1 = dbsession.query(Blogs).order_by(Blogs.comment.desc()).limit(count).offset(start).all()
            elif rank == 'likes':
                result1 = dbsession.query(Blogs).order_by(Blogs.likes.desc()).limit(count).offset(start).all()
        elif state == 'myweb':  # 我的微博
            result1 = dbsession.query(Blogs).order_by(Blogs.time.desc()).filter(
                Blogs.user_id == session.get('userid')).limit(count).offset(start).all()
        else:
            # 我的消息，先查消息表中的博客id,再查博客表
            BlogIds = OpMessages().find_by_userids(session.get('userid'))
            print(BlogIds)
            result1 = dbsession.query(Blogs).order_by(Blogs.time.desc()).filter(Blogs.id.in_(BlogIds)).limit(
                count).offset(start).all()
            print(result1)
        if not result1:
            return [], [], []
        else:
            likes = OpLikes()
            # result3 = likes.find_by_blogids(result1)
            # result2 = OpComments().find_by_blogids(result1)
            if userid is None or userid == '':
                userid = 0
            result4 = likes.find_blogids_by_userid(userid)
            result5 = OpFollowers().find_by_userids(userid)
            return result1, result4, result5
