'''
列表中的数据类型要一致才能排序
直接在源列表进行排序

my_list.sort()  默认升序
my_list.sort(reverse = True)  降序

排序
sorted(列表)  不会影响源列表,返回新列表
sorted(列表, reverse = True) 降序

列表倒置,原列表不变,返回新列表
[::-1]
列表倒置,直接修改原列表
reverse()
'''

list1 = [1, 2, 5, 6, 8, 4, 3, 5, 1, 2, 5, 4, 5]
# 默认升序
list1.sort()
print(list1)            # [1, 1, 2, 2, 3, 4, 4, 5, 5, 5, 5, 6, 8]

# 降序
list1.sort(reverse = True)
print(list1)            # [8, 6, 5, 5, 5, 5, 4, 4, 3, 2, 2, 1, 1]
print('-' * 50)

# sorted(列表)  不会影响源列表,返回新列表
list1 = [1, 2, 5, 6, 8, 4, 3, 5, 1, 2, 5, 4, 5]
list2 = sorted(list1)
# 转置
list3 = sorted(list1, reverse = True)
print(list1)            # [1, 2, 5, 6, 8, 4, 3, 5, 1, 2, 5, 4, 5]
print(list2)            # [1, 1, 2, 2, 3, 4, 4, 5, 5, 5, 5, 6, 8]
print(list3)            # [8, 6, 5, 5, 5, 5, 4, 4, 3, 2, 2, 1, 1]
print('-' * 50)


# 使用切片倒置列表,会返回新列表,旧列表不变
list4 = ['a', 'b', 'c', 'd', 'e']
list5 = list4[::-1]
print(list4)            # ['a', 'b', 'c', 'd', 'e']
print(list5)            # ['e', 'd', 'c', 'b', 'a']

# 原列表直接倒置
list6 = ['a', 'b', 'c', 'd', 'e']
list6.reverse()
print(list6)            # ['e', 'd', 'c', 'b', 'a']
