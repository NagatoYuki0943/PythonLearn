'''
单引号
双引号
三单引号
三双引号

在 python 中,字符串可以乘上一个整数,
字符串 * num  复制几份
'''

name = 'abcdefg'
sex = "futa"
hobby = '''pantyhose'''
print(name, sex, hobby)

# 如果字符串本身包含单引号,使用双引号定义,如果包含双引号可以使用单引号定义,或者统一使用三引号定义
my_name = "my nane is 'Cortex'"


#  复制几份
new_sex = sex * 3
print(new_sex)  # futafutafuta

