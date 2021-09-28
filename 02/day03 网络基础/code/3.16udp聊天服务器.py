'''
一.功能:
1.发送信息
2.接收信息
3.退出系统

二.框架的设计
1.发送信息 send_msg()
2.发送信息 recv_msg()
3.主入口   main()
4.当程序独立运行的时候,才启动聊天服务器

三.实现步骤
1.发送信息 send_msg()
    (1).定义变量接收用户与输入方的ip地址
    (2).定义变量接收用户与输入方的端口号
    (3).定义变量接收用户与输入接收方内容
    (4).使用socket.send()发送信息

2.接收信息 recv_msg()
    (1).使用socket.revcfrom()获取数据
    (2).解析数据
    (3).显示输出

3. 主入口main()
    (1).创建套接字
    (2).绑定端口
    (3).打印菜单
    (4),接收用户输入的选项
    (5).判断用户的选择,并且调用对应的函数
    (6).关闭套接字

可以自己发送给自己,socket有缓存,可以存放信息
'''

import socket


def send_msg(udp_socket):
    # (1).定义变量接收用户与输入方的ip地址
    ipaddr = input('请输入对方的ip地址:')
    # 判断是否需要默认
    if len(ipaddr) == 0:
        ipaddr = '192.168.1.103'
        print('当前默认对方ip地址为:192.168.1.103')


    # (2).定义变量接收用户与输入方的端口号
    port = input('请输入对方的端口号:')
    # 判断是否需要默认
    if len(port) == 0:
        port = 8080
        print('当前默认对方端口为:8080')

    # (3).定义变量接收用户与输入接收方内容
    data = input("请输入要发送的内容:")


    # (4).使用socket.send()发送信息
    udp_socket.sendto(data.encode(), (ipaddr, int(port)))



def recv_msg(udp_socket):
    print('正在等待数据...')
    # (1).使用socket.revcfrom()获取数据
    data,ip = udp_socket.recvfrom(1024)
    # (2).解析数据
    data = data.decode(encoding='gbk')
    # (3).显示输出
    print('数据到达:')
    print(f'data:{data}, ip:{ip}\n\n')


def main():
    # (1).创建套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # (2).绑定端口 参数1自己的ip可以不写,参数2必须写
    udp_socket.bind(('', 8081))

    while True:
        # (3).打印菜单
        print('*******************************')
        print('********** 1.发送信息 ***********')
        print('********** 2.接收信息 ***********')
        print('********** 3.退出系统 ***********')
        print('*******************************')

        # (4), 接收用户输入的选项
        select = int(input('请输入选项:'))

        # (5).判断用户的选择, 并且调用对应的函数
        if (select == 1):
            # 调用发送信息的函数
            send_msg(udp_socket)

        elif (select == 2):
            # 调用接收信息的函数
            recv_msg(udp_socket)

        elif (select == 3):
            print("退出系统")
            break


    # (6).关闭套接字
    udp_socket.close()


if __name__ == '__main__':
    main()
