# 通过 sys.path 将父目录添加进环境变量中
import sys
sys.path.append("../")

from utils import forward
from func.func import backward

forward()
# forward

backward()
# backward
