"""
下标,可以用于字符串
整数下标 从左到右从 0 开始    0  1  2  3
负数下标 从右到左从 -1开始   -4 -3 -2 -1
"""

str1 = "abcdefg"

print(str1[1])  # b
print(str1[-1])  # g

list1 = [1, 2, ["a", "b", 3]]
print(list1[2][0])  # a
print(list1[-2])  # 2

"""
len() 得到字符串长度
"""
print(len(str1))  # 7
