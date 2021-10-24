'''
函数名是特殊变量
保存特殊地址
'''

def test():
    print("哈哈哈")


test()

res = test
print(res)  # <function test at 0x000002C61C3E2EA0>
# 函数名是特殊变量
print(test) # <function test at 0x000002C61C3E2EA0>

# 输出地址10进制
print(id(res))  # 2172572413600
# 输出id16进制
print("%x" % id(res))   # 2c61c3e2ea0