'''

'''
import random

while True:
    # 1.用户出拳
    user = int(input('请输入出的拳:1(石头) 2(剪刀) 3(布): '))

    # 2.电脑随机
    # 产生随机数
    computer = random.randint(1, 3)

    # 3. 判断
    # 3.1  == 平局
    # user 胜利  user == 1 and computer == 2  || user ==2 and computer == 3 || user ==3 and computer == 1
    if user == computer:
        print('平局')
    elif (user == 1 and computer == 2) or (user == 2 and computer == 3) or (user == 3 and computer == 1):
        print('你赢了')
        #赢了就打断循环
        break
    else:
        print('电脑赢了')
