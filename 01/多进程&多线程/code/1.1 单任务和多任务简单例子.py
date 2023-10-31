'''
# 创建多任务                            函数名
p1 = multiprocessing.Process(target=sing)

# 启动多进程
p1.start()

# 等待子进程执行完毕
p1.join()

# 终止进程
p1.terminate()   # Terminate process; sends SIGTERM signal or uses TerminateProcess()
p1.kill()        # Terminate process; sends SIGKILL signal or uses TerminateProcess()

# 关闭进程
p1.close()
'''

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

    # 创建多任务                         函数名
    p1 = multiprocessing.Process(target=sing)
    p2 = multiprocessing.Process(target=dance)

    # 多进程下run方法启动相当于直接调用函数，并没有真正意义上使用多进程，这一点我们可以通过pid看的出来。而start启动却是真正意义上调用了多进程，同样我们可以通过pid看的出来
    # p1.run()

    # 启动多进程
    p1.start()
    p2.start()

    # 等待子进程执行完毕
    p1.join()
    p2.join()

    # 要在 join / terminate / kill 之后再调用 close
    p1.terminate()   # Terminate process; sends SIGTERM signal or uses TerminateProcess()
    p1.kill()        # Terminate process; sends SIGKILL signal or uses TerminateProcess()
    p1.close()       # This method releases resources held by the Process object. It is an error to call this method if the child process is still running.

    print('Interval:', time.time() - start)
    # 唱歌。。。
    # 跳舞。。。
    # 唱歌。。。
    # 跳舞。。。
    # 唱歌。。。
    # 跳舞。。。
    # Interval: 1.6125640869140625
