'''
# 创建多任务                            函数名
sing1 = multiprocessing.Process(target=sing)

# 启动多进程
sing1.start()

# 等待子进程执行完毕
sing1.join()
'''

# 进程包
import multiprocessing
import time


def sing():
    for i in range(3):
        print("唱歌。。。")
        time.sleep(0.5)


def dance():
    for i in range(3):
        print("跳舞。。。")
        time.sleep(0.5)


if __name__ == '__main__':
    start = time.time()

    # 创建多任务                            函数名
    sing1 = multiprocessing.Process(target=sing)
    dance1 =  multiprocessing.Process(target=dance)

    # 多进程下run方法启动相当于直接调用函数，并没有真正意义上使用多进程，这一点我们可以通过pid看的出来。而start启动却是真正意义上调用了多进程，同样我们可以通过pid看的出来

    # 启动多进程
    sing1.start()
    dance1.start()

    # 等待子进程执行完毕
    sing1.join()
    dance1.join()

    print('Interval:', time.time() - start)    
    # 唱歌。。。
    # 跳舞。。。
    # 唱歌。。。
    # 跳舞。。。
    # 唱歌。。。
    # 跳舞。。。
    # Interval: 1.6125640869140625
        