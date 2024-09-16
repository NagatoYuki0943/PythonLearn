"""
无论是在外面直接建立对象,还是在内层建立对象再返回,都是在外面创建txt
"""

from utils.Touch import Touch


def get_touch():
    Touch("./1.txt")
