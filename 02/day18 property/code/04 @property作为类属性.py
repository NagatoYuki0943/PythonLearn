"""
BAR = property(get_bar, set_bar, del_bar, "BAR是Foo一个属性")
# 前三个是方法名,最后是字符串
# 第1个 当通过对象访问 foo.BAR          时调用第2个方法
# 第2个 当通过对象访问 foo.BAR = ??     时调用第2个方法
# 第3个 当通过对象访问 del foo.BAR      时调用
# 第4个 当通过类名访问 Foo.BAR.__doc__  时调用
"""


class Foo(object):
    # get_bar 方法
    def get_bar(self):
        return "老铁"

    # propterty 对象
    # 四个参数全是方法名
    # 第1个 当我们访问 foo.BAR 时调用第2个方法
    # 第2个 当 foo.BAR = ?? 时调用第2个方法
    # 第3个 当 del foo.BAR 时调用
    # 第4个 当 foo.BAR.__doc__ 时调用
    BAR = property(get_bar)


foo = Foo()

# foo.get_bar == get_bar
print(foo.BAR)  # 老铁
