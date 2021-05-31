'''
replace
字符串替换,不会替换新的字符串

my_str.replace(old_str,new_str,count)
old_str: 旧字符串
new_str: 新字符串
count:   替换总数,默认全部替换
返回值,得到新的字符串,不会替换新的字符串
'''
old_str = 'hello world itcast and itcastcpp'
res = old_str.replace('itcast', '黑马')
print(old_str)  # hello world itcast and itcastcpp
print(res)      # hello world 黑马 and 黑马cpp

# 参数3: 替换次数
res1 = old_str.replace('itcast', '黑马', 1)
print(res1)     # hello world 黑马 and itcastcpp
