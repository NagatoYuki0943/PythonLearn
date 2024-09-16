"""
字典自带 copy 方法

字典是简单不可变类型,是深拷贝 dict1 = {'age': 10}

字典是复杂可变类型,是浅拷贝   dict1 = {"age": [1, 2]}
"""


def simpltDict():
    """
    字典是简单不可变类型,是深拷贝
    """

    dict1 = {"age": 10}

    dict2 = dict1.copy()

    print("dict1 =", dict1, id(dict1))
    print("dict2 =", dict2, id(dict2))
    # dict1 = {'age': 10} 2544252235136
    # dict2 = {'age': 10} 2544252235640

    dict2["age"] = 11

    print("dict1 =", dict1, id(dict1))
    print("dict2 =", dict2, id(dict2))
    # dict1 = {'age': 10} 2544252235136
    # dict2 = {'age': 11} 2544252235640     只会影响自己,是深拷贝


simpltDict()


def complexDict():
    """
    字典是复杂可变类型,是浅拷贝
    """

    dict1 = {"age": [1, 2]}

    dict2 = dict1.copy()

    print("dict1 =", dict1, id(dict1))
    print("dict2 =", dict2, id(dict2))
    # dict1 = {'age': [1, 2]} 1700771016064     地址不同
    # dict2 = {'age': [1, 2]} 1700771016136

    dict2["age"][0] = 11

    print("dict1 =", dict1, id(dict1))
    print("dict2 =", dict2, id(dict2))
    # dict1 = {'age': [11, 2]} 1700771016064    地址不同,不过里面的列表相同,说明里面的内容是浅拷贝
    # dict2 = {'age': [11, 2]} 1700771016136


# complexDict()
