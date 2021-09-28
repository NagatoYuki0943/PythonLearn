

# 1.导入模块
import os
import socket

# 2.创建套接字
tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 3.建立连接
tcp_client_socket.connect(('192.168.1.103', 8081))

# 4.接收用户输入的文件名
file_name = input('请输入下载的文件名:')

# 5.发送文件名到服务器端
tcp_client_socket.send(file_name.encode())

# 6.创建二进制文件,并且准备保存,二进制文件不能写编码
# with open 不用close
with open('C:/Users/Frostbite/Desktop/' + file_name, 'wb') as file:
    # 7.接收服务器端发送的数据,保存到本地
    # 判断文件是否传送完毕
    while True:
        file_data = tcp_client_socket.recv(1024)
        if file_data:
            file.write(file_data)
        else:
            break

# 8.关闭套接字
tcp_client_socket.close()