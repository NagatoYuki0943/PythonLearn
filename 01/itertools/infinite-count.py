# 无限迭代器（Infinite Iterators）
# count([start=0, step=1]) 接收两个可选整形参数，
# 第一个指定了迭代开始的值，第二个指定了迭代的步长。
# 此外，start参数默认为0，step参数默认为1，
# 可以根据需要来把这两个指定为其它值，或者使用默认参数


from itertools import count
import time


for i in count(10, 10):
    print(i)
    time.sleep(1)
