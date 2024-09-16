l1 = [1, 3, 5.3, 9.1, 10]

l1.sort()
print(l1)  # [1, 3, 5.3, 9.1, 10]
l1.sort(reverse=True)
print(l1)  # [10, 9.1, 5.3, 3, 1]
print("*" * 50)

l2 = [
    {"name": "Taobao", "age": 100},
    {"name": "Runoob", "age": 7},
    {"name": "Google", "age": 100},
    {"name": "Wiki", "age": 200},
]

# 按照年龄排序
l2.sort(key=lambda x: x["age"])
print(
    l2
)  # [{'name': 'Runoob', 'age': 7}, {'name': 'Taobao', 'age': 100}, {'name': 'Google', 'age': 100}, {'name': 'Wiki', 'age': 200}]
print("*" * 50)


d1 = {1: "a", 2: "b", 4: "c", -1: "d"}
d1.update({9: "e"})
print(d1)  # {1: 'a', 2: 'b', 4: 'c', -1: 'd', 9: 'e'}

# 字典排序,keys,values,items
print(sorted(d1))  # [-1, 1, 2, 4, 9]
print(sorted(d1.keys()))  # [-1, 1, 2, 4, 9]
print("*" * 50)

print(sorted(d1.values()))  # ['a', 'b', 'c', 'd', 'e']
print("*" * 50)

print(sorted(d1.items()))  # [(-1, 'd'), (1, 'a'), (2, 'b'), (4, 'c'), (9, 'e')]
print(
    sorted(d1.items(), key=lambda x: x[0])
)  # [(-1, 'd'), (1, 'a'), (2, 'b'), (4, 'c'), (9, 'e')]
print(
    sorted(d1.items(), key=lambda x: x[1])
)  # [(1, 'a'), (2, 'b'), (4, 'c'), (-1, 'd'), (9, 'e')]
