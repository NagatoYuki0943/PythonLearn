import re

# re.findall(pattern, string, flags=0)
# 或
# pattern.findall(string[, pos[, endpos]])
# 参数：
# - pattern 匹配模式。
# - string 待匹配的字符串。
# - pos 可选参数，指定字符串的起始位置，默认为 0。
# - endpos 可选参数，指定字符串的结束位置，默认为字符串的长度。


print(re.findall(r"\d+", "runoob 123 google 456"))  # ['123', '456']

pattern = re.compile(r"\d+")  # 查找数字
print(pattern.findall("runoob 123 google 456"))  # ['123', '456']
print(pattern.findall("run88oob123google456", pos=0, endpos=10))  # ['88', '12']

print("*" * 50)


iter = re.finditer(r"\d+", "runoob 123 google 456")
for i in iter:
    print(i.group())
print("-" * 50)
# 123
# 456

pattern = re.compile(r"\d+")  # 查找数字
iter = pattern.finditer("runoob 123 google 456")
for i in iter:
    print(i.group())
print("-" * 50)
# 123
# 456

iter = pattern.finditer("run88oob123google456", pos=0, endpos=10)
for i in iter:
    print(i.group())
# 88
# 12
