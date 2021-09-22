'''
Counter是一个dict子类，主要是用来对你访问的对象的频率进行计数
'''

from collections import Counter


ls = [2, 3, 4, 2, 4, 4, 5, 3, 1, 4, 9, 0, 1, 0, 15, 0]
lr = [2, 3, 1, 0, 4, 0]


res = Counter(ls)
print(res)
# Counter({4: 4, 0: 3, 2: 2, 3: 2, 1: 2, 5: 1, 9: 1, 15: 1})

# 获取4的次数
print(res[4])   # 4

# 全部元素
print(res.elements())
# <itertools.chain object at 0x00000206AA4DAC50>
print(list(res.elements()))
# [2, 2, 3, 3, 4, 4, 4, 4, 5, 1, 1, 9, 0, 0, 0, 15]


# Counter之间可以相加减,可以对次数相加减
ret = Counter(lr)
print(res + ret)
# Counter({4: 5, 0: 5, 2: 3, 3: 3, 1: 3, 5: 1, 9: 1, 15: 1})

print(res - ret)
# Counter({4: 3, 2: 1, 3: 1, 5: 1, 1: 1, 9: 1, 0: 1, 15: 1})