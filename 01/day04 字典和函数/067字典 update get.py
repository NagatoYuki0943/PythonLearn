'''
字典是无序的,通过下标取值,修改值

字典 dict 定义使用 {},由键值对构成 C++ map
变量 = {key1:value1, key2:value2, key3:value3...}  key:value是一个键值对
字典的key 可以是一个字符串类型或数字类型(int float),不能是一个列表,必须是不可变类型  bool,int,float,string,tuple
value可以为任何值

my_dict[key] 获取 value值,没有key值会报错
my_dict.get(key) 使用get获取值,没有key值返回None

参数2是默认值
get(value,default)

len()获取键值对数量
'''

# 1.定义空字典
dict1 = {}
dict2 = dict()
print(dict1, type(dict1))  # {} <class 'dict'>
print(dict2, type(dict2))  # {} <class 'dict'>
print("*" * 50)


# 2.定义带数据的字典
dict3 = {'name': 'Tom', 'age': 18, 'hobby': ['pantyhose', 'sticks', 'stocking']}
print(dict3)  # {'name': 'Tom', 'age': 18, 'hobby': ['pantyhose', 'sticks', 'stocking']}


# 3.添加新数据,数据要写成字典格式
dict3.update({'length':100})
print(dict3)  # {'name': 'Tom', 'age': 18, 'hobby': ['pantyhose', 'sticks', 'stocking'], 'length': 100}


# 访问value值,字典中没有下标概念,使用key值访问value值
print(dict3['name'])  # Tom
print(dict3['hobby'][0])    # pantyhose
# print(dict3['a'])         # key值不存在,会报错

# get方式获取不会报错,没有返回None
# get(key)
print(dict3.get('name'))    # Tom
print(dict3.get('a'))       # None

# get(value,default)
print(dict3.get('a', 'HHHH'))  # HHHH
print("*" * 50)


# 4.使用len获取长度,获取键值对的数量
print(len(dict3))  # 4
