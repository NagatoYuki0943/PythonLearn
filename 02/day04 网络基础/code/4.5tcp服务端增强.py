'''
循环接收条信息,
循环接受多个客户端连接
bug:前面的客户端不退出,后面的没法连接
'''

import socket

# 1.创建服务端
tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# 2.绑定ip 端口
tcp_server_socket.bind(('192.168.1.103', 8081))


# 3.设置被动监听模式
tcp_server_socket.listen(128)


while True:
    # 4.等待连接
    new_client_socket, client_ip_port = tcp_server_socket.accept()
    print(f'新客户端上线了:{client_ip_port}')

    while True:
        # 6.使用新的套接字收发数据
        new_client_socket.send('AAAAAAAAA'.encode())

        # 当接收到的数据为空的时候,表示客户端已经断开连接了,服务端也要断开
        data = new_client_socket.recv(128)
        if data:
            print(data.decode('gbk'))
        else:
            # 7. 关闭连接
            print('客户端已经断开连接')
            break

    new_client_socket.close()


tcp_server_socket.close()