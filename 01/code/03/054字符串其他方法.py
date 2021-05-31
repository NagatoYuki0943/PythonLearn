my_str = 'hello world itcast and itcastcpp'

# capitalize 把字符串的第一个字符大写
print(my_str.capitalize())  # Hello world itcast and itcastcpp


#title 把字符串的每个单词首字母大写
print(my_str.title())   # Hello World Itcast And Itcastcpp


# upper 转换 mystr 中的小写字母为大写
print(my_str.upper())   # HELLO WORLD ITCAST AND ITCASTCPP


# lower 转换 mystr 中所有大写字符为小写
print(my_str.lower())   # hello world itcast and itcastcpp


# startswith(hello) 检查字符串是否是以 hello 开头, 是则返回 True，否则返回 False
print(my_str.startswith('hello')) # True


# endswith(obj) 检查字符串是否以obj结束，如果是返回True,否则返回 False.
print(my_str.endswith('hello')) # False


# ljust(width) 返回一个原字符串左对齐,并使用空格填充至长度 width 的新字符串
print(my_str.ljust(50))


# rjust(width) 返回一个原字符串右对齐,并使用空格填充至长度 width 的新字符串
print(my_str.rjust(50))


# center(width) 返回一个原字符串居中,并使用空格填充至长度 width 的新字符串
print(my_str.center(50))


# strip() 删除 mystr 字符串两端的空白字符,包括 空格 \t \n  后面这样的字符会字节删除
my_str= '     hello     '
print(my_str.strip())


# lstrip() 删除 mystr 左边的空白字符
my_str= '     hello    '
print(my_str.lstrip())


# rstrip() 删除 mystr 右边的空白字符
my_str= '     hello     '
print(my_str.lstrip())


# partition  把mystr以str分割成三部分,str前，str和str后
my_str= 'My name is Cook'
print(my_str.partition('name'))     # ('My ', 'name', ' is Cook')


# rpartition  类似于 partition()函数,不过是从右边开始.
my_str= 'My name is Cook'
print(my_str.rpartition('name'))    # ('My ', 'name', ' is Cook')


# splitlines 按照行分隔，返回一个包含各行作为元素的列表
my_str= 'Hello\nWorld'
print(my_str.splitlines())          # ['Hello', 'World']


# isalpha   如果 mystr 所有字符都是字母 则返回 True,否则返回 False  有空格也为假
my_str= 'My name is Cook'
print(my_str.isalpha()) # False


# isdigit   如果 mystr 只包含数字则返回 True 否则返回 False.
my_str= '842'
print(my_str.isdigit()) # True


# isalnum   如果 mystr 所有字符都是字母或数字则返回 True,否则返回 False
my_str= '842aaf'
print(my_str.isalnum()) # True


# isspace   如果 mystr 中只包含空格，则返回 True，否则返回 False.
my_str= ' '
print(my_str.isspace()) # True

