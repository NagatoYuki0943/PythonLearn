'''
列表推导式,为了快速生成一个列表
1. 变量 = [生成数据的规则 for 临时变量 in xxx ]
    每循环一次,就会创建一个数据

2. 变量 = [生成数据的规则 for 临时变量 in xxx if xxx]
    每循环一次,并且if条件为True,就会创建一个数据

3. 变量 = [生成数据的规则 for 临时变量 in xxx for j in xxx]
    第二个for循环执行一次,就生成一次数据    生成数量是  i * j


字典推导式
1. 变量 = {key规则:value规则 for 临时变量 in xxx }

2. 变量 = {key规则:value规则 for 临时变量 in xxx if xxx }

3. 变量 = [key规则:value规则 for 临时变量 in xxx for j in xxx]
    dict3 = {i: j for i in range(3) for j in range(3)}   生成数量是3,因为key值相同就修改数据了
'''


# 列表推导式
# 1. 变量 = [生成数据的规则 for 临时变量 in xxx ]
#     每循环一次,就会创建一个数据
list1 = [i for i in range(5)]
print(list1)        # [0, 1, 2, 3, 4]


list2 = ['hello' for i in range(5)]
print(list2)        # ['hello', 'hello', 'hello', 'hello', 'hello']


list3 = [f'num:{i+1}' for i in list1]
print(list3)        # ['num:1', 'num:2', 'num:3', 'num:4', 'num:5']
print('*' * 50)


# 2. 变量 = [生成数据的规则 for 临时变量 in xxx if xxx]
#     每循环一次,并且if条件为True,就会创建一个数据
list4 = [i for i in range(10) if i % 2 == 0]
print(list4)        # [0, 2, 4, 6, 8]
print('*' * 50)


# 3. 变量 = [生成数据的规则 for 临时变量 in xxx for j in xxx]
#     第二个for循环执行一次,就生成一次数据
list5 = [(i,j) for i in range(3) for j in range(2)]
print(list5)        # [(0, 0), (0, 1), (1, 0), (1, 1), (2, 0), (2, 1)]
print('*' * 50)


# 字典推导式
# 1. 变量 = {key规则:value规则 for 临时变量 in xxx }
dict1 = {i: i+1 for i in range(3)}
print(dict1)        # {0: 1, 1: 2, 2: 3}
print('*' * 50)


# 2. 变量 = {key规则:value规则 for 临时变量 in xxx if xxx }
dict2 = {i: i+1 for i in range(15) if i % 3 == 0}
print(dict2)        # {0: 1, 3: 4, 6: 7, 9: 10, 12: 13}
print('*' * 50)


# 3. 变量 = [key规则:value规则 for 临时变量 in xxx for j in xxx]
dict3 = {i: j for i in range(3) for j in range(3)}
print(dict3)        # {0: 2, 1: 2, 2: 2}
print('*' * 50)


dict4 = {f"{i}{j}": j for i in range(3) for j in range(3)}
print(dict4)        # {'00': 0, '01': 1, '02': 2, '10': 0, '11': 1, '12': 2, '20': 0, '21': 1, '22': 2}
print('*' * 50)

