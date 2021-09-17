'''
输入 input()
input() 函数得到的内容就是字符串

输出 print() 函数 %s
f-string
'''

name = input('请输入姓名:')

print('姓名是%s' % name)

print(f"姓名: {name}")

# f字符串输出小数位数
num = 15.624
print(f'num: {num:.2f}')    # num: 15.62