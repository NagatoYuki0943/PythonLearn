"""
将多个字典放到一起,不过不会形成新的字典,但可以使用字典的操作
一个 ChainMap 将多个字典或者其他映射组合在一起，创建一个单独的可更新的视图。
如果没有 maps 被指定，就提供一个默认的空字典 。`ChainMap`是管理嵌套上下文和覆盖的有用工具。

"""

from collections import ChainMap


d1 = {"apple": 1, "banana": 2}
d2 = {"orange": 2, "apple": 3, "pike": 1}
combined_d = ChainMap(d1, d2)
reverse_combined_d = ChainMap(d2, d1)

print(combined_d)
print(reverse_combined_d)
# ChainMap({'apple': 1, 'banana': 2}, {'orange': 2, 'apple': 3, 'pike': 1})
# ChainMap({'orange': 2, 'apple': 3, 'pike': 1}, {'apple': 1, 'banana': 2})


# 重复的键不会多次获取
for k, v in combined_d.items():
    print(k, v)
    # apple 1
    # pike 1
    # banana 2
    # orange 2
print("-" * 50)


for k, v in reverse_combined_d.items():
    print(k, v)
    # orange 2
    # banana 2
    # apple 3
    # pike 1
