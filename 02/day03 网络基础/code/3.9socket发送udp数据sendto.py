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
# udp_socket.sendto(数据,ip和端口)
# 数据必须是二进制格式     字符串.encode()
# ip和端口必须是是元组，（“ip地址”, 端口号）     地址参数必须是元组
str = 'Hello World'
udp_socket.sendto(str.encode(), ('192.168.1.159', 8080))


# 4.关闭套接字
udp_socket.close()