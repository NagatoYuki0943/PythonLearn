"""
删除数据

pop(key) 取出值,返回value    删除不存在的值会报错

根据key值删除数据             删除不存在的值会报错
del my_dict[key]

直接删除字典
del my_dict

删除全部
clear()
"""

dict = {"name": "Tom", "age": 18, "hobby": ["pantyhose", "sticks", "stocking"]}


# pop(key, default_value) 弹出指定的key值,没有就返回默认值,否则报错
# pop(key) 取出值,返回value
name = dict.pop("name")
print(name)  # Tom
print(dict)  # {'age': 18, 'hobby': ['pantyhose', 'sticks', 'stocking']}
# dict.pop('aaa')               # 删除不存在的值会报错,除非有默认值
print(dict.pop("sex", "male"))  # male,默认值
print("*" * 50)


# del删除值
del dict["age"]
# del dict['sex']    #删除不存在的值会报错
print(dict)  # {'name': 'Tom', 'hobby': ['pantyhose', 'sticks', 'stocking']}
print("*" * 50)


# 删除里面列表的值
hobby1 = dict["hobby"].pop()
print(hobby1)  # stocking
print(dict)  # {'hobby': ['pantyhose', 'sticks']}
print("*" * 50)


# clear删除全部
dict["sex"] = "futa"
dict.clear()
print(dict)  # {}
print("*" * 50)


# 直接删除字典
dict = {"name": "Tom", "age": 18, "hobby": ["pantyhose", "sticks", "stocking"]}
del dict
# print(dict)       # 报错,没有它了
