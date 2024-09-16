# https://zhuanlan.zhihu.com/p/100459723
import fire


def add(x, y):
    return x + y


def multiply(x, y):
    return x * y


if __name__ == "__main__":
    fire.Fire(
        {
            "add": add,
            "mul": multiply,
        }
    )
    # python fire_test3.py add 20 30
    # 50
    # python fire_test3.py mul 20 30
    # 600
