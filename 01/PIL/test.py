"""
无法导入: 将PIL文件夹放到项目目录即可
"""

from matplotlib import pyplot as plt

from PIL import Image

image = Image.open("./image/71479714_p0.jpg")

image.show()
