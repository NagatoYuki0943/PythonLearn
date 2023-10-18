'''
python中使用不同目录的函数,
函数的相对路径是调用时调用文件的路径,不是被调用文件的路径
无论是直接调用函数还是在类里面调用函数,都是在外层创建txt文件
'''


def loss_write(number):
    with open('./loss.txt', mode='a', encoding='utf-8') as loss:
        #                      记着换行
        loss.write(str(number) + '\n')


if __name__ == "__main__":
    loss_write(1)