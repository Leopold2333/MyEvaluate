from common.dboperate import Messages
from common.dboperate import get_session
from dao.users import OpUsers

dbsession = get_session()


# ��װ��Ϣ��Ĳ���
class OpMessages:
    def commit(self):
        dbsession.commit()

    # �����ߵ�id �Ǹ��б�
    def insert_n(self, blogids, receivers):
        print(blogids, receivers)
        result1 = OpUsers().find_users_by_ids(receivers)
        for item in result1:
            print(item.id,item.username)
            message = Messages(userid=item.id, blogid=blogids,username=item.username)
            dbsession.add(message)
        self.commit()

    # ���ݲ���idȫɾ��
    def delete_by_blogid(self, blogid):
        messages = dbsession.query(Messages).filter(Messages.blogid == blogid).all()
        [dbsession.delete(i) for i in messages]
        self.commit()

    # ͨ��������id�������еĲ���id,����һ���б�
    def find_by_userids(self, receivers):
        row = dbsession.query(Messages).filter(Messages.userid == receivers).all()
        re = []
        for i in row:
            re.append(i.blogid)
        return re

    def find_Aite_by_blogid(self, blogid):
        row = dbsession.query(Messages).filter(Messages.blogid == blogid).all()
        return row