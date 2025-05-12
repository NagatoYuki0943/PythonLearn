# 在类的变量或者函数名字前面加上两个下划线，表示该函数为私有函数，只能在类的内部调用。

import uuid


class User:
    def __init__(self):
        self._id = uuid.uuid4()
        self.__id = uuid.uuid4()

    # 虚假的私有方法
    def _get_id(self):
        return self.__id

    # 真正的私有方法
    def __get_id(self):
        return self.__id


user = User()

try:
    print(f"{user._id = }")
    print(f"{user.__id = }")
except AttributeError:
    print("AttributeError: 'User' object has no attribute '__id'")
# user._id = UUID('82855722-03d1-4211-bff9-2f51e133dc63')
# AttributeError: 'User' object has no attribute '__id'


try:
    print(f"{user._get_id() = }")
    print(f"{user.__get_id() = }")
except AttributeError:
    print("AttributeError: 'User' object has no attribute '__get_id'")
# user._get_id() = UUID('82855722-03d1-4211-bff9-2f51e133dc63')
# AttributeError: 'User' object has no attribute '__get_id'
