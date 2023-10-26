'''
调用自己
终止条件
递归会大量调用内存
'''


def calc(a):
    if a >= 100:
        return a
    a += calc(a + 1)
    return a


res = calc(1)
print(res)      # 5050


def age(num):
    if(num <= 1):
        return 18
    return 2 + age(num - 1)


res = age(3)
print(res)      # 22



