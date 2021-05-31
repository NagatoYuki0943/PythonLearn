'''
集合,set,使用 {单纯地数据}
1.集合中的数据必须是不可变类型 bool,int,float,string,tuple
2.集合是可变类型
3.集合是无序的,不能使用下标,数据添加顺序和输出顺序是否一致(和C++中自动排序不同)
4.集合中的数据没有重复,可以去重

添加 add(值)

删除指定元组  remove(值)

从尾部随机删除,没有参数 pop()

清空 clear()

修改数据,先删除remove,再添加add


列表去重
list1 = [1, 3, 4, 5, 1, 4, 3, 0]
list2 = list(set(list1))

集合,列表,元组可以互相进行转换
'''

# set1 = {1, 2, [3, 5]} 报错
set1 = {1, 2, 5.1, 56, 1, 'aaa', True, (1, 4)}
print(set1, type(set1))             # {1, 2, 'aaa', 5.1, 56, (1, 4)} <class 'set'>  顺序不和输入不同

# 删除指定元组  remove(值)
set1.remove(5.1)                    # {1, 2, 56, 'aaa', (1, 4)}
print(set1)

# 从尾部随机删除,没有参数 pop()
res = set1.pop()
print(res)                          # 1
print(set1)                         # {2, 56, 'aaa', (1, 4)}

# 添加 add(值)
set1.add(15)
print(set1)                         # {2, 56, 'aaa', (1, 4), 15}

# 清空 clear()
set1.clear()
print(set1)                         # set()

# 修改数据,先删除remove,再添加add
print('*' * 50)



list1 = [1, 3, 4, 5, 1, 4, 3, 0]
list2 = list(set(list1))
print(list2)                        # [0, 1, 3, 4, 5]