# 无限迭代器（Infinite Iterators）
# cycle(iterable) 是用一个可迭代对象中的元素来创建一个迭代器，
# 并且复制自己的值，一直无限的重复下去


from itertools import cycle
import time


dataloader = [1, 2, 3]

for i in cycle(dataloader):
    print(i)  # 具有无限的输出，可以按ctrl+c来停止。
    time.sleep(1)


# 另一种实现方式
# https://github.com/lucidrains/denoising-diffusion-pytorch/blob/main/denoising_diffusion_pytorch/denoising_diffusion_pytorch.py#L58
def cycle1(dl):
    while True:
        for data in dl:
            yield data


# for i in cycle1(dataloader):
#     print(i)
#     time.sleep(1)
