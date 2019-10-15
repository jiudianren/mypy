# _*_ coding: utf-8 _*_
# author jiudianren
# time:2019/8/19 10:18

import datetime
def test_date():
    #从字符串获取时间
    str_p = '2019-01-30 15:29:08'
    dateTime_p = datetime.datetime.strptime(str_p, '%Y-%m-%d %H:%M:%S')
    #获取时分秒
    print("min:{0}".format(dateTime_p.minute))
    print(dateTime_p)  # 2019-01-30 15:29:08

    #获取当前时间
    now_data = datetime.datetime.now()
    print("now date {0}".format(now_data))
    # 时间偏移
    offset = datetime.timedelta(days=1)
    date_time_add = now_data+ offset
    print("offset：{0}，offset date: {1}".format(offset, date_time_add))
    offset = datetime.timedelta(days=-1)
    date_time_sub = now_data+ offset
    print("offset：{0}，offset date: {1}".format(offset, date_time_sub))

    #时间比较
    if date_time_add < date_time_sub:
        print("erro")
    else:
        print("{0}>{1}".format(date_time_add,date_time_sub ))

    #获取整点时间
    wholehoure =datetime.datetime(now_data.year, now_data.month, now_data.day,
                                 now_data.hour,0, 0)
    print("wholehoure:{0}".format(wholehoure))

    # 获取间隔时间
    time_rang = []
    data_time = wholehoure
    offset = datetime.timedelta(minutes=30)
    end_time = wholehoure + offset
    while data_time <= end_time:
            time_rang.append(data_time)
            data_time += datetime.timedelta(minutes=10)
    print("time range:{0}".format(time_rang))


if __name__ == "__main__":
    test_date()
