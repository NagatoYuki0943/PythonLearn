#  1. yield from 等价于 for + yield
def gen_a():
    yield 1
    yield 2
    yield 3


def gen_b():
    yield "start"

    # 把 gen_a() 产生的值全部转发出去
    yield from gen_a()
    # 等价下面的写法
    # for x in gen_a():
    #     yield x

    yield "end"


for x in gen_b():
    print(x)
print()
print()
# start
# 1
# 2
# 3
# end


# 2.yield from 也可以接普通可迭代对象
# 不一定非要接 generator，列表、元组、字符串都行
def gen():
    yield from [1, 2, 3]
    yield from ("a", "b")
    yield from "XY"


for x in gen():
    print(x)
print()
print()
# 1
# 2
# 3
# a
# b
# X
# Y


# 3. 实用例子：递归展开嵌套列表
def flatten(items: list):
    for item in items:
        if isinstance(item, list):
            yield from flatten(item)
        else:
            yield item


data = [1, [2, 3], [4, [5, 6]], 7]

for x in flatten(data):
    print(x)
print()
print()
# 1
# 2
# 3
# 4
# 5
# 6
# 7


# 4. 更关键的例子：接收子生成器的 return 值
# yield from 不只是“转发 yield”，它还能拿到子生成器最后的 return 值。
def subgen():
    yield 1
    yield 2
    # 这个返回值会变成 yield from 表达式的结果。
    return "subgen done"


def main_gen():
    result = yield from subgen()
    yield f"result = {result}"


for x in main_gen():
    print(x)
# 1
# 2
# result = subgen done
