'''
运行错误给出的运行提示
异常的组成:
异常类型: 异常具体的描述信息

'''

#f = open('1.txt', 'r', encoding="utf-8")
# FileNotFoundError: [Errno 2] No such file or directory: '1.txt'
# 找不到文件类型: 没这个文件或文件夹


print("其他的代码")
num = input("请输入一个数字:")
res = 10 / int(num)
print("计算得到的结果是:" + str(res))

# ZeroDivisionError: division by zero
# ValueError: invalid literal for int() with base 10: 'a'


print("其他的代码")