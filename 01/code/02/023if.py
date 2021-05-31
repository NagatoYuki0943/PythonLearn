'''
if 判断条件:
    判断条件为 True,会执行的代码
    判断条件为 True,会执行的代码
    ...

需要 : 符号 和 强制缩进
'''

age = input('请输入年龄:')
# 类型转换,不然没法转换
age = int(age)


if age >= 18:
    print('欢迎大爷')
else:
    print('滚蛋')

# 这里是if之外的区域
print('结束了')