import re

# \W 是除了数字字母下划线
print(re.split('\W+', 'aa, bb, cc.'))       # ['runoob', 'runoob', 'runoob', '']

print(re.split('(\W+)', ' aa, bb, cc.'))    # ['', ' ', 'runoob', ', ', 'runoob', ', ', 'runoob', '.', '']

# 只分裂两次
print(re.split('\W+', ' aa, bb, cc.', 1))   # ['', 'aa, bb, cc.']


# 对于一个找不到匹配的字符串而言，split 不会对其作出分割,但是会警告
print(re.split('a*', 'hello world'))   
# D:\Anaconda3\envs\ai\lib\re.py:212: FutureWarning: split() requires a non-empty pattern match.
#   return _compile(pattern, flags).split(string, maxsplit)
# ['hello world']

print('-' * 50)


# 可以使用compile
pattern = re.compile('\W+')
print(pattern.split('aa, bb, cc'))      # ['aa', 'bb', 'cc']


print('*' * 50)


# re.sub() 检索和替换
# re.sub(pattern, repl, string, count=0, flags=0)
# - pattern : 正则中的模式字符串。
# - repl : 替换的字符串，也可为一个函数。
# - string : 要被查找替换的原始字符串。
# - count : 模式匹配后替换的最大次数，默认 0 表示替换所有的匹配。
# - flags : 编译时用的匹配模式，数字形式。

phone = "2004-959-559 # 这是一个电话号码"
 
# 删除注释
num = re.sub(r'#.*$', "", phone)
print ("电话号码 : ", num)
# 电话号码 :  2004-959-559 

# 移除非数字的内容
num = re.sub(r'\D', "", phone)
print ("电话号码 : ", num)
# 电话号码 :  2004-959-559 

print('-' * 50)


# 将匹配的数字乘于 2
def double(matched):
    value = int(matched.group('value'))
    return str(value * 2)
 
s = 'A23G4HFD567'
print(re.sub(r'(?P<value>\d+)', double, s))
# A46G8HFD1134 数字变为2倍

print(re.search(r'(?P<value>\d+)', s).span())
# (1, 3) 找到第一个位置

print('-' * 50)


# 使用compile
# 移除非数字的内容
pattern = re.compile(r'\D')
#                 替换内容
print(pattern.sub('', phone))   # 2004959559




