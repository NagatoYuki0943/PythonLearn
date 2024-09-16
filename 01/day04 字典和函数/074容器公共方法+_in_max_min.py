"""
+           支持 字符串、列表、元组进行操作， 得到一个新的容器              不支持字典
* 整数       复制n份， 支持 字符串、列表、元组进行操作 得到一个新的容器       不支持字典
in/not in   判断存在或者是不存在，支持 字符串、列表、元组、字典进行操作，
                注意： 如果是字典的话，判断的是 key 值是否存在或不存在
max/min     返回容器中的最大/最小值
                对于字典来说，比较的字典的 key值的大小
                a < z  A < Z  A < a
"""

str1 = "My name is "
str2 = "Tom"
print(str1 + str2)  # My name is Tom
print(str2 * 5)  # TomTomTomTomTom
print("To" in str2)  # True
print(max(str1))  # y 按照字母顺序排序
print(min(str2))  # y 按照字母顺序排序
print("*" * 50)  # T  大写字母小于小写字母


list1 = ["a", "b", 1]
list2 = [1, 2]
print(list1 + list2)  # ['a', 'b', 1, 1, 2]
print(list2 * 5)  # [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]
print(1 not in list2)  # False
print(max(list2))  # 2 不同类型不能比较
print(min(list2))  # 1
print("*" * 50)


dict1 = {"a": 10, "b": 0, "c": 90}
dict2 = {"a": 10, "d": 45, "e": -90}
# print(dict1 + dict2)  字典不能相加
# print(dict1 * 5)      报错
# in 按照 key 查找
print("a" in dict1)  # True
print(10 in dict1)  # False
print(max(dict1))  # c
print(min(dict1))  # a
