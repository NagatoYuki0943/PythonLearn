import re

# re.match 尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none。
# re.match(pattern, string, flags=0)
# - pattern: 匹配的正则表达式
# - string: 要匹配的字符串。
# - flags: 标志位，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等等。

# 找到使用 .span() 返回位置
print(re.match('www', 'www.baidu.com'))
# <_sre.SRE_Match object; span=(0, 3), match='www'>

# group()/group(0) 返回字符串位置索引
print(re.match('www', 'www.baidu.com').group()) # www

# span() 返回字符串位置索引
print(re.match('www', 'www.baidu.com').span())  # (0, 3)

# start() 返回字符串开始范围
print(re.match('www', 'www.baidu.com').start()) # 0

# end() 返回字符串结束位置
print(re.match('www', 'www.baidu.com').end())   # 3

print(re.match('com', 'www.baidu.com'))          # None


print('*' * 50)



# group(num=0) 匹配的整个表达式的字符串，group() 可以一次输入多个组号，在这种情况下它将返回一个包含那些组所对应值的元组。
# groups()     返回一个包含所有小组字符串的元组，从 1 到 所含的小组号。

line = "Cats are smarter than dogs"
# 开始的r是为了让正则更明显
# .* 表示任意匹配除换行符（\n、\r）之外的任何单个或多个字符
# (.*?) 表示"非贪婪"模式，只保存第一个匹配到的子串
# re.M: 多行匹配，影响 ^ 和 $
# re.I: 使匹配对大小写不敏感
matchObj = re.match( r'(.*) are (.*?) .*', line, re.M|re.I)

if matchObj:
   print("matchObj.group() : ", matchObj.group())      # 返回全部匹配
   print("matchObj.group(1) : ", matchObj.group(1))    # 返回上面第一个 () 的匹配
   print("matchObj.group(2) : ", matchObj.group(2))    # 返回上面第二个 () 的匹配
else:
   print("No match!!")

# matchObj.group() :  Cats are smarter than dogs
# matchObj.group(1) :  Cats
# matchObj.group(2) :  smarter

print('*' * 50)


# re.search 扫描整个字符串并返回第一个成功的匹配。
print(re.search('www', 'www.runoob.com').span())  # 在起始位置匹配
print(re.search('com', 'www.runoob.com').span())  # 不在起始位置匹配
# (0, 3)
# (11, 14)

print('*' * 50)


line = "Cats are smarter than dogs"
# 开始的r是为了让正则更明显
# .* 表示任意匹配除换行符（\n、\r）之外的任何单个或多个字符
# (.*?) 表示"非贪婪"模式，只保存第一个匹配到的子串
# re.M: 多行匹配，影响 ^ 和 $   
# re.I: 使匹配对大小写不敏感
searchObj = re.search( r'(.*) are (.*?) .*', line, re.M|re.I)
 
if searchObj:
   print("searchObj.group() : ", searchObj.group())
   print("searchObj.group(1) : ", searchObj.group(1))
   print("searchObj.group(2) : ", searchObj.group(2))
else:
   print("Nothing found!!")
# searchObj.group() :  Cats are smarter than dogs   
# searchObj.group(1) :  Cats
# searchObj.group(2) :  smarter

print('*' * 50)


# re.match 只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回 None，
# 而 re.search 匹配整个字符串，直到找到一个匹配。


line = "Cats are smarter than dogs"
 
# re.M: 多行匹配，影响 ^ 和 $   
# re.I: 使匹配对大小写不敏感
matchObj = re.match( r'dogs', line, re.M|re.I)
if matchObj:
   print("match --> matchObj.group() : ", matchObj.group())
else:
   print("No match!!")
# No match!!

matchObj = re.search( r'dogs', line, re.M|re.I)
if matchObj:
   print("search --> matchObj.group() : ", matchObj.group())
else:
   print("No match!!")
# search --> matchObj.group() :  dogs

