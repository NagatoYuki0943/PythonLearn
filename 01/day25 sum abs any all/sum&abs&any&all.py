'''
sum() 列表求和
'''
print(sum([1, 2, 3]))   # 6
print("=" * 50)



'''
abs() 函数返回数字的绝对值。
'''
print("abs(-1)", abs(-1))
print("abs(0)", abs(0))
print("abs(1)", abs(1))
print("=" * 50)


'''
all() 函数用于判断给定的可迭代参数 iterable 中的所有元素是否都为 TRUE，如果是返回 True，否则返回 False。
元素除了是 0、空、None、False 外都算 True。
'''     
# 等价于：
def func1(iterable):
    for element in iterable:
        if not element:
            return False
    return True

print(all([1, 2, 3]))           # True
print(all([1, 2, 0]))           # False
print(all(["c", "a", ""]))      # False
print(all(["c", "a", None]))    # False
print(all(["c", True, False]))  # False
print("=" * 50)


'''
any() 函数用于判断给定的可迭代参数 iterable 是否全部为 False，则返回 False，如果有一个为 True，则返回 True。
元素除了是 0、空、FALSE 外都算 TRUE。
'''
# 等价于：
def func2(iterable):
    for element in iterable:
        if element:
            return True
    return False

print(any([1, 2, 3]))           # True
print(any([0, 0, 0]))           # False
print(any(["c", "a", ""]))      # True
print(any([0, False, None]))    # False
print("=" * 50)
