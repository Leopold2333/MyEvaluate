# coding: gbk
import datetime


def get_now_time():
    sys_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    sys_time = datetime.datetime.strptime(sys_time, '%Y-%m-%d %H:%M:%S')
    return sys_time


# ����һ��ʱ����ϵͳ��ǰʱ��Ƚ�
def count_time(_time):
    print(f'���ݿ��¼��ʱ��: {_time}')
    # print(type(time1))

    # һСʱ���ʱ��
    unlock_time = _time + datetime.timedelta(hours=1)
    unlock_time.ctime()
    print(f'Ӧ������ʱ��: {unlock_time}')
    # print(type(unlock_time))

    # ϵͳ��ǰʱ��
    sys_time = get_now_time()
    print(f'ϵͳ��ǰʱ��: {sys_time}')
    print(type(sys_time))

    # ����ʱ�����ϵͳʱ����ζ�Ż�����
    if unlock_time > sys_time:
        print('True')
        return True, (unlock_time - sys_time).seconds
    else:
        print('False')
        return False, 0
