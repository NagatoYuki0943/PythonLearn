# all 等价
def all_(iterable) -> bool:
    for element in iterable:
        if not element:
            return False
    return True


# any 等价
def any_(iterable) -> bool:
    for element in iterable:
        if element:
            return True
    return False


# 列表list,元素都不为空或0
print(all(['a', 'b', 'c', 'd']))    # True
print(all_(['a', 'b', 'c', 'd']))   # True
print(any(['a', 'b', 'c', 'd']))    # True
print(any_(['a', 'b', 'c', 'd']))   # True

# 列表list,存在一个为空的元素
print(all(['a', 'b', '', 'd']))     # False
print(all_(['a', 'b', '', 'd']))    # False
print(any(['a', 'b', '', 'd']))     # True
print(any_(['a', 'b', '', 'd']))    # True

# 元组tuple,元素都不为空或0
print(all(('a', 'b', 'c', 'd')))    # True
print(all_(('a', 'b', 'c', 'd')))   # True
print(any(('a', 'b', 'c', 'd')))    # True
print(any_(('a', 'b', 'c', 'd')))   # True

# 元组tuple,存在一个为空的元素
print(all(('a', 'b', '', 'd')))     # False
print(all_(('a', 'b', '', 'd')))    # False
print(any(('a', 'b', '', 'd')))     # True
print(any_(('a', 'b', '', 'd')))    # True

# 列表list,存在一个为0的元素
print(all([0, 1, 2, 3]))            # False
print(all_([0, 1, 2, 3]))           # False
print(any([0, 1, 2, 3]))            # True
print(any_([0, 1, 2, 3]))           # True

# 元组tuple,存在一个为0的元素
print(all((0, 1, 2, 3)))            # False
print(all_((0, 1, 2, 3)))           # False
print(any((0, 1, 2, 3)))            # True
print(any_((0, 1, 2, 3)))           # True

# 列表list,元素全为0,'',false
print(all([0, '', False]))          # False
print(all_([0, '', False]))         # False
print(any([0, '', False]))          # False
print(any_([0, '', False]))         # False

# 元组tuple,元素全为0,'',false
print(all((0, '', False)))          # False
print(all_((0, '', False)))         # False
print(any((0, '', False)))          # False
print(any_((0, '', False)))         # False

# # 空列表
print(all([]))                      # True
print(all_([]))                     # True
print(any([]))                      # False
print(any_([]))                     # False

# # 空元组
print(all(()))                      # True
print(all_(()))                     # True
print(any(()))                      # False
print(any_(()))                     # False
