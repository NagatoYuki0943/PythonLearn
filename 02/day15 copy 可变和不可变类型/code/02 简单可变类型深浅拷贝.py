'''
可变类型（mutable），创建后可以继续修改对象的内容（值）
    字典，列表

简单可变类型: [1, 2, 3]

简单可变类型的数据不管深拷贝还是浅拷贝，都会产生新的空间，而且保持各自的独立性
如果拷贝的是对象,连同子对象也会被拷贝


import copy
# 浅拷贝
copy.copy()
# 深拷贝
copy.deepcopy()

'''

import copy


def eq():
    '''
    直接等号赋值相当于起别名,两个变量指向相同的内存地址,会相互影响
    '''

    list1 = [1, 2, 3]


    # 直接赋值就是相同数据,一个修改了另一个也会被修改
    list2 = list1
    list2.append(4)

    print("list1=", list1, id(list1))   # list2= [1, 2, 3, 4] 1888252962760
    print("list2=", list1, id(list2))   # list2= [1, 2, 3, 4] 1888252962760

#eq()


def shallow():
    '''
    copy.copy()
    可变类型浅拷贝也会产生新的空间,能够保持各自的独立性
    '''

    list1 = [1, 2, 3]

    print('*' * 50)

    # 浅拷贝
    list2 = copy.copy(list1)
    list2.append(4)

    print("list1=", list1, id(list1))   # list1= [1, 2, 3] 1888252962760
    print("list2=", list2, id(list2))   # list3= [1, 2, 3, 4] 1888253013384

    print('*' * 50)

# shallow()


def deep():
    '''
    copy.deepcopy()
    可变类型浅拷贝产生新的空间,能够保持各自的独立性
    '''
    
    list1 = [1, 2, 3]
    
    # 深拷贝
    list2 = copy.deepcopy(list1)

    print("list1=", list1, id(list1))   # list1= [1, 2, 3] 1231290723848
    print("list2=", list2, id(list2))   # list2= [1, 2, 3] 1231290723784

    print('*' * 50)


    list2.append(4)

    print("list1=", list1, id(list1))   # list1= [1, 2, 3] 1231290723848
    print("list2=", list2, id(list2))   # list2= [1, 2, 3, 4] 1231290723784

deep()