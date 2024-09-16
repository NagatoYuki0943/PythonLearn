"""
for 循环默认遍历 key

.keys() 获取所有key, 返回类型是dict_keys
# 1.可以使用list()类型转换转换为列表类型
# 2.可以使用for循环进行遍历

.values() 获取所有的value值,返回类型是dict_values
# 1.可以使用list()类型转换转换为列表类型
# 2.可以使用for循环进行遍历

.items() 获取键值对,返回类型是dict_items,key和value组成元组
元组通过下标 0 1 获取值
或者通过拆包(结构赋值获取)
    for k,v in res:
        pass
"""

dict = {"name": "Tom", "age": 18, "hobby": ["pantyhose", "sticks", "stocking"]}


# for 循环默认遍历 key
for key in dict:
    print(key)
    print(dict[key])
print()
print("*" * 50)
# name
# Tom
# age
# 18
# hobby
# ['pantyhose', 'sticks', 'stocking']


# .keys() 获取所有key, 返回类型是dict_keys
# 1.可以使用list()类型转换转换为列表类型
# 2.可以使用for循环进行遍历
res = dict.keys()
print(res, type(res))  # dict_keys(['name', 'age', 'hobby']) <class 'dict_keys'>

for key in res:
    print(dict[key], end=" ")  # Tom 18 ['pantyhose', 'sticks', 'stocking']
print()
print("*" * 50)


# .values() 获取所有的value值,返回类型是dict_values
# 1.可以使用list()类型转换转换为列表类型
# 2.可以使用for循环进行遍历
res = dict.values()
print(
    res, type(res)
)  # dict_values(['Tom', 18, ['pantyhose', 'sticks', 'stocking']]) <class 'dict_values'>
for value in res:
    print(value, end=" ")  # Tom 18 ['pantyhose', 'sticks', 'stocking']
print()
print("*" * 50)


# .items() 获取键值对,返回类型是dict_items,key和value组成元组
res = dict.items()
print(
    res, type(res)
)  # dict_items([('name', 'Tom'), ('age', 18), ('hobby', ['pantyhose', 'sticks', 'stocking'])]) <class 'dict_items'>
for item in res:
    print(
        item[0], item[1], end=" "
    )  # name Tom age 18 hobby ['pantyhose', 'sticks', 'stocking']
print()
print("*" * 50)


# 拆包,就是结构赋值
for k, v in res:
    print(k, v)
# name Tom
# age 18
# hobby ['pantyhose', 'sticks', 'stocking']
