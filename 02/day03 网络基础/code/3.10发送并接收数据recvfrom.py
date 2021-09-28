'''

'''
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
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


# 3.发送数据
udp_socket.sendto('test'.encode(), ('192.168.1.103', 8080))


# 4.接收二进制数据
# recv_data = udp_socket.recvfrom(1024)   每次接收1024个字节
# recv_data 是一个元组
# 1）第一个元素  收到的数据的二级制
# 2）第二个元素  元组,发送方的ip和端口
# 返回值是元组: 字符串和发送的ip和端口
# (b'二进制字符串', ('192.168.1.103', 8080))
#
# 此方法会造成程序阻塞,等待另一台计算机发送数据,如果对方发送数据,recefrom会接触阻塞,如果对方没法送数据,会一直等待

recv_data = udp_socket.recvfrom(1024)
# 数据的二进制格式
print(recv_data[0])                     # b'\xc4\xe3\xba\xc3'
# 数据解码,gbk是为了中文不报错
print(recv_data[0].decode('gbk'))       # 你好
# 元组,对方ip和端口
print(recv_data[1])                     # ('192.168.1.103', 8080)


# 5.关闭套接字
udp_socket.close()