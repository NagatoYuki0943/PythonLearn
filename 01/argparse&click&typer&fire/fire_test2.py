# https://zhuanlan.zhihu.com/p/100459723
import fire


def add(x, y):
    return x + y


def multiply(x, y):
    return x * y


if __name__ == "__main__":
    fire.Fire()
    # python fire_test2.py add 10 20
    # 30
    # python fire_test2.py multiply 10 20
    # 200
