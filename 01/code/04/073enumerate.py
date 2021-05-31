'''
enumerate 主要针对列表
找到列表的下标和值,使用遍历查找出来

'''
list = ['a', 'b', 'c', 'd', 'e']

for i in list:
    # index查找数据的下标,里面填写值就可以
    print(list.index(i), i)
# 0 a
# 1 b
# 2 c
# 3 d
# 4 e

# 直接使用enumerate()获取下标和列表
for j in enumerate(list):
    print(j)
# (0, 'a')
# (1, 'b')
# (2, 'c')
# (3, 'd')
# (4, 'e')