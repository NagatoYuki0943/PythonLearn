"""
提前建立连接了,因此发送和接收数据都不用再写地址了

建立连接                ("服务端ip", 服务端端口)
tcp_client_socket.connect(('192.168.1.103', 8080))

发送数据
tcp_client_socket.send("tcp你好".encode())

接收数据 返回二进制数据
recv_data = tcp_client_socket.recv(1024)

"""

# 1.导入模块
import socket


# 2.创建套接字
# socket.socket(协议类型,传输方式)
# 参数一：
# socket.AF_INET 使用IPv4
# socket.AF_INET6 使用IPv6
# 参数二：
# socket.SOCK_DGRAM 使用UDP的传输方式（无连接）
# socket.SOCK_STREAM 使用TCP的传输方式（有连接）
tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# 3.建立连接                ("服务端ip", 服务端端口)
tcp_client_socket.connect(("192.168.1.103", 8080))


# 4.发送数据
tcp_client_socket.send("tcp你好".encode())


# 5.接收数据 返回二进制数据
recv_data = tcp_client_socket.recv(1024)
print(recv_data)  # b'\xb0\xa1'
print(recv_data.decode("gbk"))  # 啊


# 6.关闭连接
tcp_client_socket.close()
