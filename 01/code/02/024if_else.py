'''
if 判断条件:
    判断条件为 True,会执行的代码
    判断条件为 True,会执行的代码
    ...
else:
    判断条件为 False, 会执行的代码
    判断条件为 False, 会执行的代码
    .....

if 和 else 只会执行其中的一个,
'''

age = input('请输入年龄:')

if int(age) >= 18:
    hobby= input('请输入爱好:')

    if hobby == 'pantyhose':
        print('prprprprpr')
    else:
        print('ok')
else:
    print('小屁孩滚蛋')
