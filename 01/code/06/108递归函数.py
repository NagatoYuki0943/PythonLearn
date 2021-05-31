'''

'''


def factorial1(n):
    res = 1
    # range参数2,要+1,不然数字小1
    for i in range(1, n + 1):
        res *= i
    print(res)

factorial1(5)


def factorial2(n):
    if n <= 1:
        return 1

    return n * factorial2(n - 1)

res = factorial2(5)
print(res)