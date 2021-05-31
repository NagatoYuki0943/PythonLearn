'''
可以打多个断点
点击debug
然后点击下面第一个或者第三个就一步一步执行

'''

age = input('请输入年龄:')
age = int(age)

if age >= 18:
    hobby= input('请输入爱好:')

    if hobby == 'pantyhose':
        print('prprprprpr')
    else:
        print('ok')
else:
    print('小屁孩滚蛋')

print('if之外')