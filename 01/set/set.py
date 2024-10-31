a: set = set([1, 2, 2, 3, 3, 4, 5])
b: set = {1, 2, 2, 3, 3, 4, 5}

print(a)  # {1, 2, 3, 4, 5}
print(b)  # {1, 2, 3, 4, 5}


# 添加元素
a.add(5)
a.add(6)
print(a)  # {1, 2, 3, 4, 5, 6}


# 移除集合中的元素，且如果元素不存在，会发生错误
a.remove(5)
try:
    a.remove(7)
except KeyError:
    print("no 7")
print(a)  # {1, 2, 3, 4, 6}


# 移除集合中的元素，且如果元素不存在，不会发生错误
a.discard(7)
print(a)  # {1, 2, 3, 4, 6}


# 随机删除集合中的一个元素
a.pop()
print(a)  # {2, 3, 4, 6}


# 元素个数
print(len(a))  # 4


# 清空元素
a.clear()
print(a)  # set()
print("*" * 100)

# 浅拷贝
a: set = set([1, 2, 2, 3, 3, 4, 5])
b: set = a.copy()
print(a)  # {1, 2, 3, 4, 5}
print(b)  # {1, 2, 3, 4, 5}
a.add(6)
print(a)  # {1, 2, 3, 4, 5, 6}
print(b)  # {1, 2, 3, 4, 5}


# update
a: set = set([1, 2, 2, 3, 3, 4, 5])
b: set = set([4, 5, 6, 7, 8])
a.update(b)
print(a)  # {1, 2, 3, 4, 5, 6, 7, 8}
