"""
都直接在原列表中添加,不会返回新的列表

append(数据) 向列表尾部添加数据

insert(下标, 数据)  在指定的下标数据添加数据,其他数据往后挪

extend(可迭代对象) 会将对象中的数据逐个添加到原列表末尾
可迭代对象: 字符串,列表

list.copy() 创建列表的浅拷贝
"""

# append(数据)  向列表尾部添加数据
list = [1, 2, 3, 4]
res = list.append(5)
print(res)  # None 表示空 null
print(list)  # [1, 2, 3, 4, 5]


# insert(下标,数据)  在指定的下标数据添加数据,其他数据往后挪
list = [1, 2, 3, 4]
list.insert(1, "a")
print(list)  # [1, 'a', 2, 3, 4]


# extended()  会将对象中的数据逐个添加到原列表末尾
list = [1, 2, 3, 4]
list.extend("hel")
print(list)  # [1, 2, 3, 4, 'h', 'e', 'l']
list = [1, 2, 3, 4]
list.extend([6, "Python"])
print(list)  # [1, 2, 3, 4, 6, 'Python']


# 创建列表的浅拷贝
list1 = list.copy()
print(list1)  # [1, 2, 3, 4, 6, 'Python']
list1[0] = 0
print(list1)  # [0, 2, 3, 4, 6, 'Python']
print(list)  # [1, 2, 3, 4, 6, 'Python']

# 浅拷贝, 如果列表中的元素是可变对象, 那么浅拷贝只是复制了引用, 并没有复制对象本身, 所以修改其中一个对象会影响另一个对象
list2 = [{"name": "张三", "age": 20}, {"name": "李四", "age": 25}]
list3 = list2.copy()
print(list2)
print(list3)
# [{'name': '张三', 'age': 20}, {'name': '李四', 'age': 25}]
# [{'name': '张三', 'age': 20}, {'name': '李四', 'age': 25}]

list3[0]["age"] = 21
print(list2)
print(list3)
# [{'name': '张三', 'age': 21}, {'name': '李四', 'age': 25}]
# [{'name': '张三', 'age': 21}, {'name': '李四', 'age': 25}]
