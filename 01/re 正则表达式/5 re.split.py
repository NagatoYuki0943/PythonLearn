import re


split1 = "_"
split2 = "-"

string1 = "a_bc-d_ef-g"
# split 只能分隔一个字符
print(string1.split(split1))
print(string1.split(split2))
# ['a', 'bc-d', 'ef-g']
# ['a_bc', 'd_ef', 'g']

# re.split 可以分隔多个字符串,不同的分隔符要用 “|” 隔开
print(re.split(f"{split1}|{split2}", string1))
# ['a', 'bc', 'd', 'ef', 'g']


# 不存在分隔符不会报错
string2 = "abcdefg"
print(string2.split(split1))
print(string2.split(split2))
print(re.split(f"{split1}|{split2}", string2))
# ['abcdefg']
# ['abcdefg']
# ['abcdefg']


split3 = "<|im_end|>"
split4 = "</s>"
string3 = "abc<|im_end|>def</s>g"
print(re.split(f"{split3}|{split4}", string3))
# ['abc', '|', '|', 'def', '/s', 'g']

# 由于split3和split4中都包含|，所以Python会将其解释为正则表达式的一部分，而不是字面量的字符串。
# 为了解决这个问题，需要对split3和split4中的|进行转义，这样Python就不会将其视为正则表达式的特殊字符，
# 而是将其视为普通的字符。你可以使用re.escape函数来自动转义字符串中的所有正则表达式特殊字符。
# 使用re.escape转义split3和split4中的所有正则表达式特殊字符
escaped_split3 = re.escape(split3)
escaped_split4 = re.escape(split4)
print(escaped_split3)                   # <\|im_end\|> 增加了转义符号
print(escaped_split4)                   # </s>
print([escaped_split3, escaped_split4]) # ['<\\|im_end\\|>', '</s>']  打印数组时会多出一个转义符号
print([split3, split4])                 # ['<|im_end|>', '</s>']
print(re.split(f"{escaped_split3}|{escaped_split4}", string3))
# ['abc', 'def', 'g']
