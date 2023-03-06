'''
元组和列表类似,都可以存放多个不同数据类型的数据,
列表使用 [],元组使用()
元组中的元素不能修改,没有增删改,只有查
tulip1 = (1, 2, 3, 4, True, "GeForce")
tulip1 = 5, 6, 8        不用括号直接给一个变量多个值,也是元组

元组支持下标和切片
tulip[index]
tulip[start, end, step]

定义空元组,没有意义,因为没法修改
tuple2 = ()
tuple2 = tuple()

定义一个数据的元组
tuple3 = (3,)   要有逗号才是元组,不然是int

支持 index查询方法,没有find查询方法
index(查找值,start,end) 根据数据值,查找元素所在的下标,找到返回元素的下标,没有找到程序报错
查找值: 要找的内容
start:  开始查找位置,默认是0                 也是正数
end:    结束查找位置之后的位置,默认是 len()    也是正数


count查询出现次数
count(查找值,start,end)
查找值: 要找的内容
start:  开始查找位置,默认是0                 也是正数
end:    结束查找位置之后的位置,默认是 len()    也是正数
'''

tulip1 = (1, 2, 3, 4, True, "GeForce")
# 元组支持下标和切片
print(tulip1[0])
print(tulip1[1:4])   # (2, 3, 4)
tulip1 = 5, 6, 8
print(tulip1)        # (5, 6, 8)


# 定义空元组,没有意义,因为没法修改
tuple2 = ()
print(type(tuple2))             # <class 'tuple'>
tuple2 = tuple()
print(type(tuple2))             # <class 'tuple'>


# 定义一个数据的元组
tuple3 = (3)
print(tuple3, type(tuple3))     # 3 <class 'int'>   不是元组,是int
# 加上逗号才是元组
tuple3 = (3,)
print(tuple3, type(tuple3))     # (3,) <class 'tuple'>


tulip4 = (1, 2, 3, 4, True, "GeForce")
# 查询数据,没有find
print(tulip4.index(4))          # 3
print(tulip4.index(4, 1, 5))    # 3
#print(tulip1.index(4, 1, 3))   # 找不到会报错


# count 查询出现次数
tuple5 = (1, 2, 3, 1, True, "GeForce")
print(tuple5.count(1))  # 3   两个1和Ture 都是 1
