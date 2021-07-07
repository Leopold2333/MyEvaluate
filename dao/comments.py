from flask import session
from common.dboperate import Users
from common.dboperate import Comments
from common.dboperate import get_session

dbsession = get_session()


class OpComments:
    def commit(self):
        dbsession.commit()

    # 新增一条评论记录
    def insert(self, blogid, username, content):
        comment = Comments(userid=session.get('userid'), username=username, blogid=blogid, content=content)
        dbsession.add(comment)
        self.commit()

    # 根据博客id全删除
    def delete_by_blogid(self, blogid):
        comments = dbsession.query(Comments).filter(Comments.blogid == blogid).all()
        [dbsession.delete(i) for i in comments]
        self.commit()

    # 得到评论数量
    def get_count(self):
        return dbsession.query(Comments).count()

    # 查询所有评论
    def get_all(self):
        return dbsession.query(Comments).all()

    # 在博客id列表里查找所有对应博客id的评论
    def find_by_blogids(self, result1):
        row = dbsession.query(Comments, Users).join(Users, Users.id == Comments.user_id) \
            .order_by(Comments.time.desc()).filter(Comments.blog_id == result1[0].id).all()
        for i in range(1, len(result1)):
            row += dbsession.query(Comments, Users).join(Users, Users.id == Comments.user_id) \
                .order_by(Comments.time.desc()).filter(Comments.blog_id == result1[i].id).all()
        return row

    def find_by_blogid(self, blogid):
        return dbsession.query(Comments).order_by(Comments.time.desc()).filter(Comments.blogid == blogid).all()
