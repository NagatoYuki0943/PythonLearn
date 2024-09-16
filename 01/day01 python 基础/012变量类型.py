"""
bool
    true
    false

Number 数字
    int(有符号整形)
    long(长整形) python2中有,python统一使用int
    float(浮点型)
    complex(复数)

String 字符串

容器
    List(列表)    链表
    Tuple(元组)
    Dictionary(字典)  map

使用 type() 得到数据类型
type.print 回车 直接补全代码
"""

flag = True
print(type(flag))  # <class 'bool'>
# 如果单行注释放在代码后面,至少分隔两个空格

flag = 1
print(type(flag))  # <class 'int'>

flag = 1.5
print(type(flag))  # <class 'float'>

flag = "True"
print(type(flag))  # <class 'str'>

flag = [1, 2, 3]
print(type(flag))  # <class 'list'>
