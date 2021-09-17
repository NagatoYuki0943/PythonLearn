'''
一个大的字符串里面截取一部分内容
切片语法: [start:end:step]
start:  开始截取位置,不写默认为0
end:    结束位置后一个,不写位置直接到最后一个(前提步长是整数,如果步长是负数的话,它是第一个)
step:   步长,截取间隔,默认是1

start 和 end 能写负数,从右往左数  -1 -2 -3

my_str[:]  得到和原来一样的字符串
my_str[::-1]  字符串的倒置

不会改变原值,会返回新的值
'''
str1 = 'abcdefghijklmn'

print(str1[2:4])    # cd
print(str1[3:10:2]) # dfhj


# 不写 end 自动截取到最后
print(str1[5:])     # fghijklmn


# [:] 得到和原来一样的字符串
print(str1[:])      # abcdefghijklmn


# [] 里面可以填写负数,从右往左数,顺序没有倒转 -1 -2 -3 -4
print(str1[-5:-1])  # jklm

# end在start的前边,没数据
print(str1[3:1])    # 没数据

# end在start的前边,没数据 step为负数,从右往左找
print(str1[3:1:-1]) # dc

# [::-1]  字符串的逆置
print(str1[::-1])   # nmlkjihgfedcba

# [::2]   隔两位输出一次
print(str1[::2])    # acegikm