# 组合迭代器（Combinatoric Iterators）
# zip_longest, 和 zip 类似，按照长度最长的迭代器来组合元素，但当某个迭代器中元素不够用时，可以用 fillvalue 来填充缺失的值。


from itertools import zip_longest


name: list[str] = ["Alice", "Bob", "Charlie"]
numbers: list[int] = [1, 2, 3, 4, 5]
symbols: list[str] = ["$", "%", "&", "@"]


# 原本 zip 只会组合到长度最短的迭代器的结尾
zipped = zip(name, numbers, symbols)
for item in zipped:
    print(item)
print("\n")
# ('Alice', 1, '$')
# ('Bob', 2, '%')
# ('Charlie', 3, '&')


zipped = zip_longest(name, numbers, symbols)
for item in zipped:
    print(item)
print("\n")
# ('Alice', 1, '$')
# ('Bob', 2, '%')
# ('Charlie', 3, '&')
# (None, 4, '@')
# (None, 5, None)


zipped = zip_longest(name, numbers, symbols, fillvalue="?")
for item in zipped:
    print(item)
print("\n")
# ('Alice', 1, '$')
# ('Bob', 2, '%')
# ('Charlie', 3, '&')
# ('?', 4, '@')
# ('?', 5, '?')
