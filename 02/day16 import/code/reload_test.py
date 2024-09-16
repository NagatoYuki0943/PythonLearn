"""
import 导入模块后，如果模块被修改，此时再次 import 不起作用
    import 自动防止重复包含

强制重新加载一次模块
    from imp import reload
    reload(要重新加载的模块) # 必须是模块,不能是函数或其他

"""


def test():
    print("-------- 222222 --------")
