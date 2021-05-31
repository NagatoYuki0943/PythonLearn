'''
类型转换
将原始数据转换为需要的数据,不会改变原值,会生成一个新的数据

int(值)
float(值)
'''


# 1转换为int类型     int(值)
# 1.1 float => int
pi = 3.14
num = int(pi)
print(type(pi))     # <class 'float'>
print(type(num))    # <class 'int'>

# 1.2 整数类型字符串 => int
str1 = '3'
num1 = int(str1)
print(type(str1))   # <class 'str'>
print(type(num1))   # <class 'int'>

# 非整形就报错了
# str2 = '3.1'
# num2 = int(str2)
# str3 = '3a'
# num3 = int(str3)


# 2 转换为float
# 2.1 int => float
num2 = 10
num3 = float(num2)
print(type(num2))   # <class 'int'>
print(type(num3))   # <class 'float'>

# 2.2 数字类型字符串 => float
str4 = '23.1'
num4 = float(str4)
print(type(str4))   # <class 'str'>
print(type(num4))   # <class 'float'>

# 非数字就报错了
# str5 = '3.1a'
# num5 = float(str5)


# eval() 还原原来的数据类型,去掉字符串的引号,获取变量名,这个变量应该提前定义,不然报错
num6 = eval('100')
print(type(num6))       # <class 'int'>
num7 = eval('3.102')
print(type(num7))       # <class 'float'>
list1 = "[{'name': 'b', 'age': 14, 'gender': 'm'}]"
list1 = eval(list1)
print(list1, type(list1))   # <class 'list'>



# 就变为变量名了
# num8 = eval('num')  会报错,没有赋值
# 这样可以,因为将 num7 的值给了 num8
num8 = eval('num7')
print(num8)     # 3.102
