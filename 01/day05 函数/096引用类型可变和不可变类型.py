"""
类型的可变与不可变: 在不改变变量引用的前提下,能否改变变量中引用的数据
如果能改变时可变类型,不能改变就是不可变类型

不可变类型: bool int float str tulip(元组中放列表,就能改列表中的内容了)
可变类型:   list dict set

python中的内存优化,对于不可变类型进行的,值相同,存放数据位置就相同
"""

num1 = 10
num2 = num1
num2 = num1 + num2
print(num1, num2)  # 10 20


float1 = 10.2
float2 = float1
float2 = float2 + 1
print(float1, float2)  # 10.2 11.2


# list可变类型
list1 = [1, 2, 3]
list2 = list1
list2[0] = 99
print(list1, list2)  # [99, 2, 3] [99, 2, 3]


# dict可变类型
dict1 = {"name": "Tom", "age": 18}
dict2 = dict1
dict2["name"] = "Jerry"
print(dict1, dict2)  # {'name': 'Jerry', 'age': 18} {'name': 'Jerry', 'age': 18}


# python中的内存优化,对于不可变类型进行的,值相同,存放数据位置就相同
a = 15
b = 15
print(
    id(a) == id(b)
)  # 1994114099952 1994114099952   地址相同,python中的内存优化,对于不可变类型进行的

tuple1 = (1, 2)
tuple2 = (1, 2)
print(id(tuple1) == id(tuple2))  # True    不过在终端中就是false了
# 终端中有小整数概念 -5~255,如果是小整数,使用相同的引用地址,如果不是,会开辟新的内存空间


# list 和 dict 没有内存优化
list3 = [1, 2, 3]
list4 = [1, 2, 3]
print(id(list3) == id(list4))  # False


tuple3 = [1, 2, [3, 4]]
tuple3[2][0] = 11
print(
    tuple3
)  # [1, 2, [11, 4]]   值变了,但是修改的不是元组中的数据,元组存放的是列表地址,存放的不是数据
