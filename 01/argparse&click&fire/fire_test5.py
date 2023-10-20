# https://zhuanlan.zhihu.com/p/100459723
import fire


class BrokenCalculator(object):

    def __init__(self, offset=0):
        self._offset = offset

    def add(self, x, y):
        return x + y + self._offset

    def mul(self, x, y):
        return x * y + self._offset


if __name__ == '__main__':
    # 传递类和实例对象的基本作用是一样的，但传递类还有一个额外的特性：
    # 如果构造函数中定义了参数，那么这些参数都会作为整个命令行程序的选项参数
    fire.Fire(BrokenCalculator)
    # python fire_test5.py add 2 10
    # 12
    # python fire_test5.py --offset=2 add 2 10
    # 14
    # python fire_test5.py mul 2 10
    # 20
    # python fire_test5.py --offset=2 mul 2 10
    # 22
