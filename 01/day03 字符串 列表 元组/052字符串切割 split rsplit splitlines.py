"""
split()
字符串切割

my_str.split(substr,count)
substr: 按照什么内容分隔字符串,默认是空白字符: 空格,tab,\n
count:  切割次数,切割出的数量 = count + 1,默认全部切割
返回值: 列表[],切割的数据就没有了

rsplit 方法,从右到左

splitlines 按照行分割

"""

my_str = "hello world itcast and itcastcpp"

# 参数1: 默认是空白字符: 空格,tab,\n
res = my_str.split()
print(res)  # ['hello', 'world', 'itcast', 'and', 'itcastcpp']

res = my_str.split(" ")
print(res)  # ['hello', 'world', 'itcast', 'and', 'itcastcpp']

res = my_str.split(" ", 2)
print(res)  # ['hello', 'world', 'itcast and itcastcpp']

# 切割的数据就没有了
res = my_str.split("itcast")
print(res)  # ['hello world ', ' and ', 'cpp']

# 有 rsplit 方法,从右到左
res = my_str.rsplit("itcast", 1)
print(res)  # ['hello world itcast and ', 'cpp']

# splitlines 按照行分隔，返回一个包含各行作为元素的列表
my_str = "Hello\nWorld\n"  # splitlines可以去除单个空行
print(my_str.splitlines())  # ['Hello', 'World']
print(my_str.splitlines(keepends=True))  # ['Hello\n', 'World\n']    keepends会保留结尾

my_str = "Hello\nWorld\n\n"  # 多个空行无法去除
print(my_str.splitlines())  # ['Hello', 'World', '']
print(
    [line for line in my_str.splitlines() if line != ""]
)  # ['Hello', 'World'] 判断方式去除空格

# split可以除去多个空行
print(my_str.split())  # ['Hello', 'World']

my_str = "Hello World\nnihao zaima\n"
# split可以除去多个空行,但是会将一行中按照空格等分开
print(my_str.split())  # ['Hello', 'World', 'nihao', 'zaima']
