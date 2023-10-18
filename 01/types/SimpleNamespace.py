"""
SimpleNamespace
该类添加自Python 3.3，可以用属性访问的方式访问其名称空间。

也就是说，SimpleNamespace实例将其中的所有键都公开为类属性。因此访问属性时可以使用obj.key这样的点式语法，不需要用普通字典的obj[‘key’]方括号索引语法。

正如其名，SimpleNamespace很简单，基本上就是扩展版的字典，能够很好地访问属性并以字符串打印出来，还能自由地添加、修改和删除属性。
"""

from types import SimpleNamespace


# 1.从0初始化
a = SimpleNamespace()
print(a)
# namespace()

# 添加变量
a.name = "Tom"
a.age = 12
a.friend = ["Jerry", "Dog", "Duck"]
print(a)
# namespace(name='Tom', age=12, friend=['Jerry', 'Dog', 'Duck'])

# 修改值
a.age = 13
print(a)
# namespace(name='Tom', age=13, friend=['Jerry', 'Dog', 'Duck'])


# 2.赋值初始化
ModalityType = SimpleNamespace(
    VISION="vision",
    TEXT="text",
    AUDIO="audio",
    THERMAL="thermal",
    DEPTH="depth",
    IMU="imu",
)
print(ModalityType)
# namespace(VISION='vision', TEXT='text', AUDIO='audio', THERMAL='thermal', DEPTH='depth', IMU='imu')

print(ModalityType.VISION)
# vision
