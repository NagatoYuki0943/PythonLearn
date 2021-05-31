'''
都直接在原列表中添加,不会返回新的列表

append(数据) 向列表尾部添加数据


insert(下标, 数据)  在指定的下标数据添加数据,其他数据往后挪


extended(可迭代对象) 会将对象中的数据逐个添加到原列表末尾
可迭代对象: 字符串,列表

'''


# append(数据)  向列表尾部添加数据
list = [1, 2, 3, 4]
res = list.append(5)
print(res)          # None 表示空 null
print(list)         # [1, 2, 3, 4, 5]


# insert(下标,数据)  在指定的下标数据添加数据,其他数据往后挪
list = [1, 2, 3, 4]
list.insert(1, 'a')
print(list)         # [1, 'a', 2, 3, 4]


# extended()  会将对象中的数据逐个添加到原列表末尾
list = [1, 2, 3, 4]
list.extend('hel')
print(list)         # [1, 2, 3, 4, 'h', 'e', 'l']
list = [1, 2, 3, 4]
list.extend([6, 'Python'])
print(list)         # [1, 2, 3, 4, 6, 'Python']