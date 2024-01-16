dummy = False
if dummy:
    # 线程
    from multiprocessing.dummy import Process, Pool, Queue, Pipe, Lock
else:
    # 进程
    from multiprocessing import Process, Pool, Queue, Pipe, Lock
from queue import Empty
import torch
from torch import nn, Tensor
from torchvision import models
from torchvision import transforms
import time


"""load_data -> data_preprocess -> infer -> show_result
4个进程独立推理,使用3个queue进行数据传输
"""


def load_data(queue_out: Queue):
    """将数据放入queue

    Args:
        queue_out (Queue): 传入图片的queue
    """
    for i in range(10):
        queue_out.put(torch.randn(1, 3, 64, 64))
        time.sleep(1)


def data_preprocess(queue_in: Queue, queue_out: Queue):
    """数据预处理

    Args:
        queue_in (Queue): 获取图片
        queue_out (Queue): 返回预处理后的图片
    """
    transform = transforms.Compose([
        transforms.Normalize(
            [0.485, 0.456, 0.406],
            [0.229, 0.224, 0.225]
        ),
    ])
    try:
        while True:
            image = queue_in.get(timeout=5)
            image = transform(image)
            queue_out.put(image)
    except Empty:
        print("data_preprocess exit")
        queue_in.close()


def infer(queue_in: Queue, queue_out: Queue):
    """推理

    Args:
        queue_in (Queue): 经过数据预处理后的图片
        queue_out (Queue): 预测结果
    """
    model = models.resnet18(num_classes=1).eval()
    try:
        with torch.inference_mode():
            while True:
                image = queue_in.get(timeout=5)
                y = model(image)
                queue_out.put(y)
    except Empty:
        print("infer exit")
        queue_in.close()


def show_result(queue_in: Queue):
    """展示结果

    Args:
        queue_in (Queue): 预测结果
    """
    try:
        while True:
            y = queue_in.get(timeout=5)
            print(y)
    except Empty:
        print("show_result exit")
        queue_in.close()


def chain_infer():
    queue1 = Queue(maxsize=3)
    queue2 = Queue(maxsize=3)
    queue3 = Queue(maxsize=3)

    processes = [
        Process(target=load_data, args=(queue1,)),
        Process(target=data_preprocess, args=(queue1, queue2,)),
        Process(target=infer, args=(queue2, queue3,)),
        Process(target=show_result, args=(queue3,)),
    ]

    for p in processes:
        p.start()

    for p in processes:
        p.join()

    # tensor([[5.6034]])
    # tensor([[5.5219]])
    # tensor([[5.7969]])
    # tensor([[5.6400]])
    # tensor([[4.6440]])
    # tensor([[4.7229]])
    # tensor([[5.4668]])
    # tensor([[5.1511]])
    # tensor([[4.9672]])
    # tensor([[4.6813]])
    # data_preprocess exit
    # show_result exit
    # infer exit


def run_chain_infer():
    """套用又一层进程,假设多摄像头的情况"""
    p = Process(target=chain_infer)
    p.start()
    p.join()


if __name__ == "__main__":
    run_chain_infer()
