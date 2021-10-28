'''
python中使用不同目录的函数,
函数的相对路径是调用时调用文件的路径,不是被调用文件的路径

'''


import os
import sys
os.chdir(sys.path[0])

def loss_write(number):
    '''
    写入数据,一行一个
    '''

    with open('./records/loss.txt', mode='a', encoding='utf-8') as loss:
        #                      记着换行
        loss.write(str(number) + '\n')


if __name__ == "__main__":
    loss_write(1)