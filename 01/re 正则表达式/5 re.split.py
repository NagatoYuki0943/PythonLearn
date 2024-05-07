import re


split1 = "_"
split2 = "-"

string1 = "a_bc-d_ef-g"
# split 只能分隔一个字符
print(string1.split(split1))                    # ['a', 'bc-d', 'ef-g']
print(string1.split(split2))                    # ['a_bc', 'd_ef', 'g']

# re.split 可以分隔多个字符串,不同的分隔符要用 “|” 隔开
print(re.split(f"{split1}|{split2}", string1))  # ['a', 'bc', 'd', 'ef', 'g']

# 不存在分隔符不会报错
string2 = "abcdefg"
print(string2.split(split1))                    # ['abcdefg']
print(string2.split(split2))                    # ['abcdefg']
print(re.split(f"{split1}|{split2}", string2))  # ['abcdefg']
