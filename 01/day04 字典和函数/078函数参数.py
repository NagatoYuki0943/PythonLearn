def func(name, age, num1 = 0, num2 = 0):
    print(f"My name is {name},age is {age}")
    return num1 + num2

res = func('Tom', 18, 18, 12)
print(res)
# My name is Tom,age is 18
# 30

res = func('Jerry', 16, 10, 15)
print(res)
# My name is Jerry,age is 16
# 25