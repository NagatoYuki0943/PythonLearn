'''
直接删除原列表数据

remove(数据值) 根据数据值删除数据,删除的数据不存在就报错


pop(下标) 删除下标值,默认删除最后一个数据并返回数据,删除不存在的下标会报错


del 直接删除下标的值
del my_list[下标] 删除不存在的值就报错
'''

# remove(数据值) 根据数据值删除数据
my_list = [1, 2, 3, 4, 5]
my_list.remove(3)
# my_list.remove(3)      删除的数据不存在就报错
print(my_list)  # [1, 2, 4, 5]


# pop(下标) 删除下标值,默认删除最后一个数据
my_list = [1, 2, 3, 4, 5]
res = my_list.pop()
print(res)  # 5
print(my_list)  # [1, 2, 3, 4]
res = my_list.pop(1)
print(my_list)  # [1, 3, 4]
# my_list.pop(10)        要删除的下标不存在就报错


my_list = [1, 2, 3, 4, 5]
del my_list[0]
print(my_list)  # [2, 3, 4, 5]
# del my_list[10]        要删除的下标不存在就报错
