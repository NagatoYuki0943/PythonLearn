'''
while x
    if xxx:
        xx  # if 判断条件成立会执行
    else:
        xxx  # if 判断条件不成立,会执行
else:
    xxx  # while 循环代码运行结束(while里面的内容没有执行),但是不是被 break 终止的时候会执行


for x in xx:
    if xxx:
        xx  # if 判断条件成立会执行
    else:
        xxx  # if 判断条件不成立,会执行
else:
    xxx  # for 循环代码运行结束(for里面的内容没有执行),但是不是被 break 终止的时候会执行
'''

# 判断一个数是否是素数
i = 2
num = int(input('请输入一个数字:'))
while i <= num:
    if num % i == 0:
        print(f"{num}不是素数")
        break
    i += i

# while 循环代码运行结束(while里面的内容没有执行), 但是不是被 break 终止的时候会执行
else:
    print(f"{num}是素数")
print('===============================')



# 有一个字符串 'hello python', 想要判断这个字符串中有没有包含 p 这个字符,如果包含,就输出, 包含 p, 如果没有 p ,就输出,不包含
str = 'hello python'
for i in str:
    if i == 'p':
        print('包含p这个字符')
        break

# for 循环代码运行结束,但是不是被 break 终止的时候会执行
else:
    print('不包含这个字符')