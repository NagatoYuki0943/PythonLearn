'''
无法导入: 将PIL文件夹放到项目目录即可
'''

import os
import sys
os.chdir(sys.path[0])

from matplotlib import pyplot as plt

from PIL import Image

image = Image.open('./image/71479714_p0.jpg')

image.show()
