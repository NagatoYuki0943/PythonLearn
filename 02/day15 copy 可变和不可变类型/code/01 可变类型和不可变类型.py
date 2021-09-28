'''
可变类型（mutable），创建后可以继续修改对象的内容（值）
    字典，列表

不可变类型（immutabel） ，一旦创建就不可修改的对象（值）
    不可变类型: 数字,字符串,元组
'''


def immutabel():
    a = 5
    print("a=", a, id(a))

    a = 6
    print("a=", a, id(a))


def mutable():
    list1 = [1, 2, 3]
    print("list1=", list1, id(list1))
    list1.append(4)
    print("list1=", list1, id(list1))

    # list1= [1, 2, 3] 1975841549448    地址相同,存储在堆区
    # list1= [1, 2, 3, 4] 1975841549448


if __name__ == "__main__":
    mutable()