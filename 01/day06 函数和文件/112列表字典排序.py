'''
x是形参,是列表中的每一个数据
list.sort(key=lambda x: (排序规则1,排序规则2...)
list.sort(key=lambda x: x['name'])
list.sort(key=lambda x: (x['age'], x['name']))
'''


list = [1, 4, 3, 5, 67, 7]
list.sort()
print(list)


# 列表中是字典类型
list = [{'name': 'd', 'age': 19},
        {'name': 'b', 'age': 16},
        {'name': 'a', 'age': 16},
        {'name': 'c', 'age': 20}]


# sort参数有key:key形参,传递函数,指定规则;  reverse:翻转排序
# x是形参,是列表中的每一个数据
list.sort(key=lambda x: x['name'])
print(list)                         # [{'name': 'a', 'age': 16}, {'name': 'b', 'age': 16}, {'name': 'c', 'age': 20}, {'name': 'd', 'age': 19}]

list.sort(key=lambda x: x['age'])
print(list)                         # [{'name': 'a', 'age': 16}, {'name': 'b', 'age': 16}, {'name': 'd', 'age': 19}, {'name': 'c', 'age': 20}]

#写两个参数,当第一个排序相同,按照第二个排序
list.sort(key=lambda x: (x['age'], x['name']))
print(list)                         # [{'name': 'a', 'age': 16}, {'name': 'b', 'age': 16}, {'name': 'd', 'age': 19}, {'name': 'c', 'age': 20}]


list = ['a', 'bc', 'abc', 'def', 'ghi']
list.sort()
print(list)                         # ['a', 'abc', 'bc', 'def', 'ghi']
# 列表中字符段长度
#list.sort(key=lambda x: len(x), reverse=True)
# 简写,直接写 len 即可
list.sort(key=len, reverse=True)
print(list)                         # ['abc', 'def', 'ghi', 'bc', 'a']


