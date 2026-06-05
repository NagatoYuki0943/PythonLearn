# yield 不只是输出，还能接收值


def gen():
    x = yield "第一次暂停"
    print("收到:", x)
    return "结束返回值"


g = gen()

print(next(g))
# 第一次暂停

try:
    g.send("hello")
except StopIteration as e:
    # 生成器的 return 值会藏在 StopIteration.value 里
    print("StopIteration.value =", e.value)

# 收到: hello
# StopIteration.value = 结束返回值
