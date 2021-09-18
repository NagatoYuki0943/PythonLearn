'''
时间戳          time.time() 
获取当前时间     time.localtime()
获取格式化的时间  time.asctime()
格式化日期       time.strftime()

'''

import time
import calendar
import datetime
import math


def timeSince(since):
    # 功能:获取每次打印的时间消耗, since是训练开始的时间
    # 获取当前的时间
    now = time.time()

    # 获取时间差, 就是时间消耗
    s = now - since

    # 获取时间差的分钟数
    m = math.floor(s/60)

    # 获取时间差的秒数
    s -= m*60

    return '%dm %ds' % (m, s)




if __name__ == '__main__':

    since = time.time() - 10 * 60
    period = timeSince(since)
    print(period)

    print('*' * 50)
    print('time部分:')
    print(time.time())      
    # 1631862683.6589797
    print('*' * 50)


    # 获取当前时间
    print(time.localtime(time.time()))
    # time.struct_time(tm_year=2021, tm_mon=9, tm_mday=17, tm_hour=15, tm_min=11, tm_sec=54, tm_wday=4, tm_yday=260, tm_isdst=0)

    # 获取格式化的时间
    print(time.asctime(time.localtime(time.time())))
    # Fri Sep 17 15:13:09 2021

    # 格式化日期

    # 格式化成2021-09-17 15:14:16形式
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    
    # 格式化成Fri Sep 17 15:14:16 2021形式
    print(time.strftime("%a %b %d %H:%M:%S %Y", time.localtime())) 
    
    # 将格式字符串转换为时间戳
    a = "Sat Mar 28 22:24:24 2016"
    print(time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y")))
    # 1459175064.0



    print('*' * 50)
    print('datetime部分:')
    x = datetime.datetime.now()
    print(x)  
    # 2021-09-17 15:22:25.193045
    print(x.strftime('%a'))         # Fri
    print(x.strftime('%A'))         # Friday
    print(datetime.date.today())    # 2021-09-17



    print('*' * 50)
    print('日历部分:')
    cal = calendar.month(2016, 1)
    print ("以下输出2016年1月份的日历:")
    print (cal)
    #     January 2016
    # Mo Tu We Th Fr Sa Su
    #              1  2  3
    #  4  5  6  7  8  9 10
    # 11 12 13 14 15 16 17
    # 18 19 20 21 22 23 24
    # 25 26 27 28 29 30 31