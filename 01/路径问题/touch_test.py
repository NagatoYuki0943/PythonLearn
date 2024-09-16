"""
无论是在外面直接建立对象,还是在内层建立对象再返回,都是在外面创建txt
"""

from utils.Touch import Touch
from utils.get_touch import get_touch

if __name__ == "__main__":
    # Touch('./1.txt')    # 这样也是在外面建立1.txt
    get_touch()  # 这样也是在外面建立1.txt
