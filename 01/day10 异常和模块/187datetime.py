'''
datetime是重新封装的time模块

'''

import datetime


print(datetime.time())  # 00:00:00


print(datetime.date.today())    # 2021-05-31
print('*' * 50)


print(datetime.datetime.now())  # 2021-05-31 15:58:55.183331
print(datetime.datetime.now().year)     # 2021
print(datetime.datetime.now().month)    # 5
print(datetime.datetime.now().day)      # 31
print(datetime.datetime.now().hour)     # 16
print(datetime.datetime.now().minute)   # 0
print(datetime.datetime.now().second)   # 15




