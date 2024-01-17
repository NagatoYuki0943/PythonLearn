from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
import time
import random


# 注意,这里传递的参数只有一个,传递多个的时候只有第一个参数接收到一个tuple
def print_number(args):
    func = args[0]
    times = args[1]
    for i in range(times):
        print(f"{func} -> {i}")
        time.sleep(random.randint(0, 2))
    return args


if __name__ == "__main__":
    # 多进程要在 `if __name__ == "__main__"` 中进行,在ipynb中运行失败

    inputs = [("func1", 3), ("func2", 2), ("func3", 4), ("func4", 2)]

    with ProcessPoolExecutor(max_workers=3) as executor:
        res = executor.map(print_number, inputs)

    print("----print result----")
    for r in res:
        print(r)
