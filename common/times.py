# coding: gbk
import datetime


def get_now_time():
    sys_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    sys_time = datetime.datetime.strptime(sys_time, '%Y-%m-%d %H:%M:%S')
    return sys_time


# 传入一个时间与系统当前时间比较
def count_time(_time):
    print(f'数据库记录的时间: {_time}')
    # print(type(time1))

    # 一小时后的时间
    unlock_time = _time + datetime.timedelta(hours=1)
    unlock_time.ctime()
    print(f'应当解锁时间: {unlock_time}')
    # print(type(unlock_time))

    # 系统当前时间
    sys_time = get_now_time()
    print(f'系统当前时间: {sys_time}')
    print(type(sys_time))

    # 解锁时间大于系统时间意味着还有锁
    if unlock_time > sys_time:
        print('True')
        return True, (unlock_time - sys_time).seconds
    else:
        print('False')
        return False, 0
