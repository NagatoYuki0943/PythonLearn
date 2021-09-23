'''
1. 获取当前进程编号
    os.getpid()

2. 获取当前父进程编号
    os.getppid()

'''

# 进程包
import multiprocessing
import time
import os


def sing(name, num):
    print("唱歌进程的编号： ", os.getpid())             # 唱歌进程的编号：  22448
    print("唱歌进程的父进程的编号： ", os.getppid())     # 唱歌进程的父进程的编号：  7620

    for i in range(num):
        print(f"{name}在唱歌。。。")
        time.sleep(0.5)


def dance(name, num):
    print("跳舞进程的编号： ", os.getpid())             # 跳舞进程的编号：  19072  
    print("跳舞进程的父进程的编号： ", os.getppid())     # 跳舞进程的父进程的编号：  7620
    for i in range(num):
        print(f"{name}跳舞。。。")
        time.sleep(0.5)
        

if __name__ == '__main__':
    print("主进程的编号： ", os.getpid())   # 主进程的编号：  7620
    

    # 以元组形式传参                                  (1,) 元组一个数据也要加逗号
    s1 = multiprocessing.Process(target=sing, args=('Yuki', 3))

    # 以字典形式传参
    d1 = multiprocessing.Process(target=dance, kwargs={'name': 'Nagato', 'num': 4})
    s1.start()
    d1.start()
    # Nagato跳舞。。。
    # Yuki在唱歌。。。
    # Yuki在唱歌。。。
    # Nagato跳舞。。。
    # Yuki在唱歌。。。
    # Nagato跳舞。。。
    # Nagato跳舞。。。