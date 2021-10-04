'''
对于对象来说,无论深浅拷贝都是深拷贝

'''


import copy


class A():
    def __init__(self) -> None:
        self.name = 'A'


a = A()
b = a
b.name = 'B'


c = copy.copy(a)
c.name = 'C'

d = copy.deepcopy(a)
d.name = 'D'

print(a.name)
print(b.name)
print(c.name)
print(d.name)
# B
# B
# C
# D