dummy = False
if dummy:
    # 线程
    # 这里的 Queue 等同于 `from queue import Queue`, 是线程安全的, 有 task_done 和 join 方法
    from multiprocessing.dummy import Process, Pool, Queue, Pipe, Lock
else:
    # 进程
    # 这里的 Queue 是进程安全的
    from multiprocessing import Process, Pool, Queue, Pipe, Lock

import torch
from torch import nn, Tensor
import time


"""多进程使用不同的/共享的模型
"""

# shared model
net = nn.Linear(5, 1).eval()


def infer(data: Tensor):
    """
    Args:
        data (Tensor): [N, B, C]
    """
    # self model
    # net = nn.Linear(5, 1).eval()
    with torch.inference_mode():
        for d in data:
            # d: [B, C]
            result = net(d)
            print(result.shape)
            time.sleep(0.5)


def test_process():
    data = [torch.randn(2, 1, 5), torch.randn(3, 2, 5), torch.randn(4, 3, 5), torch.randn(5, 4, 5)]
    processes = []
    for d in data:
        process = Process(target=infer, args=(d, ))
        process.start()
        processes.append(process)
    for process in processes:
        process.join()
    # [2, 1]
    # [4, 1]
    # [3, 1]
    # [1, 1]
    # [2, 1]
    # [4, 1]
    # [3, 1]
    # [1, 1]
    # [2, 1]
    # [4, 1]
    # [3, 1]
    # [4, 1]
    # [3, 1]
    # [4, 1]


def test_pool():
    data = [torch.randn(2, 1, 5), torch.randn(3, 2, 5), torch.randn(4, 3, 5), torch.randn(5, 4, 5)]
    with Pool(processes=4) as pool:
        results = pool.map(infer, data)
    # [1, 1]
    # [2, 1]
    # [3, 1]
    # [4, 1]
    # [1, 1]
    # [2, 1]
    # [3, 1]
    # [4, 1]
    # [2, 1]
    # [3, 1]
    # [4, 1]
    # [3, 1]
    # [4, 1]
    # [4, 1]


if __name__ == "__main__":
    test_process()
    print("-" * 10)
    test_pool()
