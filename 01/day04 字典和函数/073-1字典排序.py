'''
x指的是一个item, x[0]是key, [1]是value
sorted(字典.items(), key=lambda x: (x[0], x[1]))

'''

d1 = {'a': 4, 'b': 2, 'c': 1, 'd': 5, 'e': 6, 'f': 0, 'g': -8}
print(d1)
# {'a': 4, 'b': 2, 'c': 1, 'd': 5, 'e': 6, 'f': 0, 'g': -8}


res = sorted(d1.keys())
print(res)
# ['a', 'b', 'c', 'd', 'e', 'f', 'g']


res = sorted(d1.values())
print(res)
# [-8, 0, 1, 2, 4, 5, 6]


# 通过key排序
res = sorted(d1.items(), key=lambda x: x[0])
print(res)
# [('a', 4), ('b', 2), ('c', 1), ('d', 5), ('e', 6), ('f', 0), ('g', -8)]


# 通过value排序
res = sorted(d1.items(), key=lambda x: x[1], reverse=True)
print(res)
# [('e', 6), ('d', 5), ('a', 4), ('b', 2), ('c', 1), ('f', 0), ('g', -8)]


l1 = [{"name": "Taobao", "age": 100},
      {"name": "Runoob", "age": 7},
      {"name": "Google", "age": 100},
      {"name": "Wiki", "age": 200}]


# 通过 age 升序排序
print("列表通过 age 升序排序: ")
print(sorted(l1, key=lambda x: x['age']))
# [{'name': 'Runoob', 'age': 7}, {'name': 'Taobao', 'age': 100}, {'name': 'Google', 'age': 100}, {'name': 'Wiki', 'age': 200}]


# 先按 age 排序，再按 name 排序
l1.sort(key=lambda x: (x['age'], x['name']))
print(l1)
# [{'name': 'Runoob', 'age': 7}, {'name': 'Google', 'age': 100}, {'name': 'Taobao', 'age': 100}, {'name': 'Wiki', 'age': 200}]
