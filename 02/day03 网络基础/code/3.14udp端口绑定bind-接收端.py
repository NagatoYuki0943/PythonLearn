"""
绑定端口,要传入一个元组
(自己的地址, 端口), 地址设为 '' 表示自己的地址(支持多个网卡)
ip地址尽可能写为"",好处当计算机由多个网卡的时候，不同网卡的数据都能被接收
udp_socket.bind(('192.168.1.103', 8081))
"""

# 引入模块
import socket


# 创建套接字
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


# 绑定端口,要传入一个地址元组
# (自己的地址, 端口), 地址设为 '' 表示自己的地址(支持多个网卡)
udp_socket.bind(("", 8081))


# 接收数据
recv_data, ip = udp_socket.recvfrom(1024)
print(recv_data.decode("gbk"))  # 哈哈哈哈
print(ip)  # ('192.168.1.103', 8080)


# 关闭连接
udp_socket.close()
