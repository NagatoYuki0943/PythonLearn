import os
import shutil
from glob import glob


files = os.listdir()


for i in files:
    if os.path.isdir(i):
        # 进入目录
        os.chdir(i)
        path = glob("*.mp4")
        # print(path)
        # ['10.1 EfficientNetV2网络详解_高清 1080P+.mp4']

        # 移动文件
        shutil.move(path[0], '../')

        # 退出目录
        os.chdir('../')
