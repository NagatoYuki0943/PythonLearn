'''
判断条件成立,执行表达式 1, 条件不成立,执行表达式 2
变量 = 表达式1 if 判断条件 else 表达式2  # 推荐使用扁平化代码
'''
a = int(input('请输入一个数字:'))
b = int(input('请输入一个数字:'))

#    表达式1 if 判断条件 else 表达式2
# res = a - b if a > b else b - a

# 括号加了更好看
res = (a - b) if (a > b) else (b - a)
print(res)
