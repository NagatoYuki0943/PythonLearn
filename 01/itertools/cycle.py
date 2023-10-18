"""
cycle, 无限重复数据
"""


from itertools import cycle
from time import sleep

dataloader = [1, 2, 3]

for i in cycle(dataloader):
    print(i)
    sleep(1)
# 1
# 2
# 3
# 1
# 2
# 3
# ...


# https://github.com/lucidrains/denoising-diffusion-pytorch/blob/main/denoising_diffusion_pytorch/denoising_diffusion_pytorch.py#L58
def cycle1(dl):
    while True:
        for data in dl:
            yield data

# for i in cycle1(dataloader):
#     print(i)
#     sleep(1)
# 1
# 2
# 3
# 1
# 2
# 3
# ...
