'''
列表数据查询
没有 find() 方法

index(查找值,start,end) 根据数据值,查找元素所在的下标,找到返回元素的下标,没有找到程序报错
查找值: 要找的内容
start:  开始查找位置,默认是0                 也是正数
end:    结束查找位置之后的位置,默认是 len()    也是正数

count(查找值,start,end)
查找值: 要找的内容
start:  开始查找位置,默认是0                 也是正数
end:    结束查找位置之后的位置,默认是 len()    也是正数


in/ont in   判断是否存在,存在True,不存在False  一般和if结合使用
substr in my_str
substr not in my_str

'''

# index(substr) 查询出现的下标
list = [5, 3.14, True, 'Ok', 5]
print(list.index(3.14))         # 1
print(list.index(3.14, 1, 4))   # 1
#print(list.index(3.13))        # 数据不存在,程序报错


# count(substr) 统计出现次数
list = [5, 3.14, True, 'Ok', 5]
print(list.count(5))            # 2


# in/ont in   判断是否存在,存在True,不存在False
list = [5, 3.14, True, 'Ok', 5]
print( 3.14 in list)            # True
print( 3.13 in list)            # False
print( 3.13 not in list)        # True
