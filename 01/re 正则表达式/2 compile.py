import re

# compile 函数用于编译正则表达式，生成一个正则表达式（ Pattern ）对象，供 match() 和 search() 这两个函数使用。
# re.compile(pattern[, flags])
# - pattern : 一个字符串形式的正则表达式
# - flags 可选，表示匹配模式，比如忽略大小写，多行模式等，具体参数为：
# - re.I 忽略大小写
#
#     - re.L 表示特殊字符集 \w, \W, \b, \B, \s, \S 依赖于当前环境
#     - re.M 多行模式
#     - re.S 即为' . '并且包括换行符在内的任意字符（' . '不包括换行符）
#     - re.U 表示特殊字符集 \w, \W, \b, \B, \d, \D, \s, \S 依赖于 Unicode 字符属性数据库
#     - re.X 为了增加可读性，忽略空格和' # '后面的注释

# 用于匹配至少一个数字
pattern = re.compile(r"\d+")
m = pattern.match("one12twothree34four")  # 查找头部，没有匹配
print(m)  # None


m = pattern.match("one12twothree34four", 2, 10)  # 从第2的位置开始匹配，没有匹配
print(m)  # None

m = pattern.match("one12twothree34four", 3, 10)  # 从第3的位置开始匹配，正好匹配
print(m)  # 返回一个 Match 对象


print(m.group(0))  # 第一个匹配到的内容
# 12
print(m.start(0))  # 开始位置
# 3
print(m.end(0))  # 结束位置
# 5
print(m.span(0))  # 匹配字符串范围
# (3, 5)

print("*" * 50)


pattern = re.compile(r"([a-z]+) ([a-z]+)", re.I)  # re.I 表示忽略大小写
m = pattern.match("Hello World Wide Web")
print(m)  # 匹配成功，返回一个 Match 对象
# <_sre.SRE_Match object; span=(0, 11), match='Hello World'>

print(m.groups())  # 等价于 (m.group(1), m.group(2), ...)
# ('Hello', 'World')

print(m.group(0))  # 返回匹配成功的整个子串
# Hello World
print(m.span(0))  # 返回匹配成功的整个子串的索引
# (0, 11)
print(m.start(0))
# 0
print(m.end(0))
# 11

print(m.group(1))  # 返回第一个分组匹配成功的子串
# Hello
print(m.span(1))  # 返回第一个分组匹配成功的子串的索引
# (0, 5)

print(m.group(2))  # 返回第二个分组匹配成功的子串
# World
print(m.span(2))  # 返回第二个分组匹配成功的子串索引
# (6, 11)

# m.group(3)          # 不存在第三个分组
# Traceback (most recent call last):
#   File "d:/Python/Pycharm/01/day13 re正则表达式/2 compile.py", line 69, in <module>
#     m.group(3)          # 不存在第三个分组
# IndexError: no such group

print("*" * 50)


pattern = re.compile(r"\d+")
s = pattern.search("a9a0k10kae")
print(s)
# <_sre.SRE_Match object; span=(1, 2), match='9'>
print(s.group())
# 9
print(s.span())  # (1, 2)
print(s.start())  # 1
print(s.end())  # 2

print("*" * 50)


pattern = re.compile(r"\d+")
f = pattern.findall("a9a0k10kae")
print(f)  # ['9', '0', '10']

print("*" * 50)


pattern = re.compile(r"\d+")
f = pattern.finditer("a9a0k10kae")
print(next(f).group())  # 9
