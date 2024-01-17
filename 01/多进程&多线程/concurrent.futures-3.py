from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
import time
import random


def return_number(number: int) -> int:
    print(f"start threading {number}")
    time.sleep(random.randint(0, 2))
    print(f"end threading {number}")
    return number


if __name__ == "__main__":
    # 多进程要在 `if __name__ == "__main__"` 中进行,在ipynb中运行失败
    with ProcessPoolExecutor(max_workers=3) as executor:
        # 返回一个生成器，遍历的结果为0,1,2,3。无论执行结果先后顺序如何，看输入的iterator顺序
        # 因为线程池为3，所以0~2进池，其中某个执行完后，3进池
        res = executor.map(return_number, range(4))

    print("----print result----")
    for r in res:
        print(r)
    # start threading 0
    # end threading 0
    # start threading 1
    # start threading 2
    # end threading 2
    # start threading 3
    # end threading 1
    # end threading 3
    # ----print result----
    # 0
    # 1
    # 2
    # 3
