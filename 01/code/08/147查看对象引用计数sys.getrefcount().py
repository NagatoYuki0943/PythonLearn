'''
查看引用计数
sys.getrefcount(对象)  显示值会比实际多一个,因为它也会调用一次

'''

import sys


class Dog(object):
    pass


dog1 = Dog()

print(sys.getrefcount(dog1))    # 2 应该是1,他会多显示一个

dog2 = dog1
print(sys.getrefcount(dog1))    # 3
print(sys.getrefcount(dog2))    # 3

del dog1
print(sys.getrefcount(dog2))    # 2