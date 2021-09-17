
# 打印7的倍数,含有7的值
for i in range(1, 101):
    if (i % 7 == 0) or (i % 10 == 7) or (i //10 ==7):
        print(i, end=" ")
    else:
        pass
print('---------------------')

# name = 'Python'
# password = '123456'
#
# while True:
#     user_name = input('请输入用户名:')
#     user_pass = input('请输入密码:')
#     if (name == user_name) and (password == user_pass):
#         print('登录成功')
#         break
#     else:
#         print('Sorry')
print('---------------------')




print('---------------------')
# 判断一个数是否是素数
i = 2
num = int(input('请输入一个数字:'))
while i <= num:
    if num % i == 0:
        print(f"{num}不是素数")
        break
    i += i
else:
    print(f"{num}是素数")
print('---------------------')



num = 2
while num <= 200:
    i = 2
    while i < num:
        if num % i == 0:
            break
        i += 1
    else:
        print(num, end=" ")
    num += 1
print()
print('---------------------')



for i in range(2, 201):
    for j in range(2, i):
        if i % j == 0:
            break
    # 循环完,都不能被整除,for里面的执行,就说明它是素数,就输出
    else:
        print(i, end=" ")

