
# 生成器函数
def my_generator():
    for x in range(10):
        yield x

# 遍历生成器
for item in my_generator():
    print(item, end=" ")
print()


# 生成器函数可以被返回
def my_generator1():
    gen = my_generator()
    print(gen)
    return gen

# 遍历生成器
for item in my_generator1():
    print(item, end=" ")
print()
