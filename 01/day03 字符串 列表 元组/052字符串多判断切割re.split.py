import re


string = "1+2-3|4"

# python内建的split()函数只能使用单个分隔符
print(string.split("-"))
# ['1+2', '3|4']

# re模块的split()函数可以使用多个分隔符对句子进行分割，其中不同的分隔符要用 "|" 隔开
print(re.split("\+|-|\|", string)) # \+ - \| 代表 + = |
# ['1', '2', '3', '4']
