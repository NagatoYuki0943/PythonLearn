import time

"""
python在向文件中保存数据时，只有脚本结束之后才会保存

缓冲区问题：
    Python的文件操作默认使用缓冲区，这意味着数据可能首先被写入到内存中的缓冲区，然后才被刷新到磁盘。
    调用flush()可以强制刷新缓冲区。
"""


# 打开文件用于写入
with open('example.txt', 'w') as file:
    for i in range(10):
        str1 = f'{i = }\n'
        print(str1, end="")
        file.write(str1)  # 写入数据
        file.flush()  # 可选：强制刷新缓冲区
        time.sleep(1)

# 文件会在with块结束时自动关闭，并且缓冲区也会被刷新
