'''
join
字符串连接 外面将里面连接在一起

my_str.join(可迭代对象)
可迭代对象: 字符串 / 列表(列表中每一个数据都是字符串)
将my_str 这个字符串添加到可迭代对象的两个元素之间
返回值: 一个新的字符串,不会改变原字符串
'''

my_str = '_'
res = my_str.join('hello')
print(res)  # h_e_l_l_o

my_str = '**'
res = my_str.join('hello')
print(res)  # h**e**l**l**o


# 自定义列表
my_list = ['aa', 'bb', 'cc', 'dd']
my_str = '_'
res = my_str.join(my_list)
print(res)  # aa_bb_cc_dd

my_str = ' '
res = my_str.join(my_list)
print(res)  # aa bb cc dd