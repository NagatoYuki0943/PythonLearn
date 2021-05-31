'''
list 列表,里面可以同时存放多种数据,和php数组很像
使用 [] 定义
'''

# 定义空列表
list1 = []
print(type(list1))  # <class 'list'>
# 也是空列表
list2 = list()
print(type(list1))  # <class 'list'>

# 定义带数据的列表
list3 = [1, 2, 3, 'a', True]
print(list3)        # [1, 2, 3, 'a', True]


# len() 列表长度
print(len(list3))   # 5


# 列表支持下标和切片操作
# 下标操作和字符串不同的是,字符串不能使用下标修改里面数据,列表可以修改
print(list3[1])     # 2
print(list3[-1])    # True
# 切片
print(list3[1:4])   # [2, 3, 'a']

# 字符串不能使用下标修改里面数据,列表可以修改
list4 = [1, 2, 3, 4, 5]
list4[1] = 'a'
list4[-1] = True
print(list4)        # [1, 'a', 3, 4, True]