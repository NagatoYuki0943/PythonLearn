'''
添加和修改都使用key值
key值存在就是修改,不存在就是添加
注意 key 值  int 1 和 float 1.0 1.00... 代表一个值


in 操作符用于判断键是否存在于字典中，如果键在字典 dict 里返回 true，否则返回 false。
not in 操作符刚好相反，如果键在字典 dict 里返回 false，否则返回 true。
'''


dict1 = {'name': 'Tom'}
# key值存在就修改
dict1['name'] = 'Jerry'
# key值不存在就添加
dict1['age'] = 18
print(dict1)            # {'name': 'Jerry', 'age': 18}
dict1[1] = 2
dict1[1.0] = 3
dict1[1.00] = 4
print(dict1)            # {'name': 'Jerry', 'age': 18, 1: 4}


# in 操作符用于判断键是否存在于字典中，如果键在字典 dict 里返回 true，否则返回 false。
# not in 操作符刚好相反，如果键在字典 dict 里返回 false，否则返回 true。
dict2 = {1:"a", 2:"b", 3:"b"}
print(1 in dict2)       # True
print(1 not in dict2)   # False
print(4 in dict2)       # False
