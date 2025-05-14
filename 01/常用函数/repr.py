"""
repr() 函数将对象转化为供解释器读取的形式，不转义字符。

f"{var!r}" 的效果也一样
"""

import re


print("\nRUNOOB\n")
#
# RUNOOB
#

print(r"\nRUNOOB\n")
# \nRUNOOB\n

s = "\nRUNOOB\n"
print(s)
#
# RUNOOB
#

# 可以正确打印出换行符, 但是和 r"" 略有不同, 这个会打印两边的 ''
print(repr(s))
# '\nRUNOOB\n'

# 可以正确打印出换行符
print(f"{s!r}")
# '\nRUNOOB\n'


split_words = ["\n*no reference.*", "\nreferences:"]
print(split_words)
# ['\n*no reference.*', '\nreferences:']

split_words = [re.escape(word) for word in split_words]

print(split_words)
# ['\\\n\\*no\\ reference\\.\\*', '\\\nreferences:']

print(repr("|".join(split_words)))
# '\\\n\\*no\\ reference\\.\\*|\\\nreferences:'  # 忽略转义字符
