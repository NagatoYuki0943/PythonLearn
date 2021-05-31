'''
split()
字符串切割

my_str.split(substr,count)
substr: 按照什么内容分隔字符串,默认是空白字符: 空格,tab,\n
count:  切割次数,切割出的数量 = count + 1,默认全部切割
返回值: 列表[],切割的数据就没有了

有 rsplit 方法,从右到左
'''
my_str = 'hello world itcast and itcastcpp'

# 参数1: 默认是空白字符: 空格,tab,\n
res = my_str.split()
print(res)  # ['hello', 'world', 'itcast', 'and', 'itcastcpp']

res = my_str.split(' ')
print(res)  # ['hello', 'world', 'itcast', 'and', 'itcastcpp']

res = my_str.split(' ', 2)
print(res)  # ['hello', 'world', 'itcast and itcastcpp']

# 切割的数据就没有了
res = my_str.split('itcast')
print(res)  # ['hello world ', ' and ', 'cpp']

# 有 rsplit 方法,从右到左
res = my_str.rsplit('itcast', 1)
print(res)  # ['hello world itcast and ', 'cpp']