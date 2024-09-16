# https://zhuanlan.zhihu.com/p/100459723
import fire


class Calculator(object):
    def add(self, x, y):
        return x + y

    def mul(self, x, y):
        return x * y


if __name__ == "__main__":
    calculator = Calculator()
    # 将类实例化，并把实例化的对象多为 fire.Fire 的入参
    fire.Fire(calculator)
    # python fire_test4.py add 5 30
    # 35
    # python fire_test4.py mul 5 30
    # 150
