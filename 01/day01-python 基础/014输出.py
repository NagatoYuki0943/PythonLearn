# python中使用print() 输出

# 基本输出
print('Hello')
print(123)

# 一次输出多个
print(1, 2, 3, 'aaa')  # 1 2 3 aaa

# 表达式
print(1 + 3)  # 4

# 格式化输出
# %s: 字符串;  %d: int;  %f: float,默认小数点6位
name = 'Tom'
print("我叫%s,我很开心" % name)  # 我叫Tom,我很开心

age = 18
print("我的年龄是%d岁" % age)  # 我的年龄是18岁

height = 170.5
print('我的身高是%f厘米' % height)  # 我的身高是170.500000厘米 小数点默认6位

# %.2f 保留两位小数
print('我的身高是%.2f厘米' % height)  # 我的身高是170.50厘米

# 多个坑位,后面变量使用 %( , , ) 添加
print('我的名字是%s,我的年龄是%d岁,我的身高是%.2f厘米' % (name, age, height))  # 我的名字是Tom,我的年龄是18岁,我的身高是170.50厘米

# 输出 % 使用 %%
success = 50
print('成功率是%d%%' % success)  # 成功率是50%


# python3.6支持 f-string,占位同一使用    f'{变量名}'   F'{变量名}'
print(f'我的名字是{name},我的年龄是{age}岁,我的身高是{height}厘米')  # 我的名字是Tom,我的年龄是18岁,我的身高是170.50厘米


# print函数输出之后会添加一个换行,如果不想要这个换行,就添加  , end='' 里面填写什么行尾就是什么
print('hello ', end='')
print('world')

# 换行输出   \n
print('Good Good\nDay Day Up')

# 输出 \
print('\\')  #


# f字符串输出小数位数
num = 15.624
print(f'num: {num:.2f}')    # num: 15.62
