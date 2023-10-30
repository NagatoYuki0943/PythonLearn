"""
repr() 函数将对象转化为供解释器读取的形式。
"""


s = '\nRUNOOB\n'
print(s)
# 
# RUNOOB
# 

# 可以正确打印出换行符
print(repr(s))  # '\nRUNOOB\n'


dict = {'runoob': 'runoob.com', 'google': 'google.com'};
print(dict)         # {'runoob': 'runoob.com', 'google': 'google.com'}
print(repr(dict))   # {'runoob': 'runoob.com', 'google': 'google.com'}
