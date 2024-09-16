"""
广播地址：xxx.xxx.xxx.255       或者    255.255.255.255
需要开启套接字权限才能发送广播

# 设置广播权限
# PermissionError: [Errno 13] Permission denied
# udp_socket.setsockopt(套接字,属性,属性值)
# socket.SOL_SOCKET 当前的套接字
# socket.SO_BROADCAST 广播属性
# True 可以发送广播
udp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, True)
"""

# 1.导入模块
import socket

# 2.创建套接字
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 3.绑定ip和端口(可选)
udp_socket.bind(("", 8081))

# 4.设置广播权限
# PermissionError: [Errno 13] Permission denied
# udp_socket.setsockopt(套接字,属性,属性值)
# socket.SOL_SOCKET 当前的套接字
# socket.SO_BROADCAST 广播属性
# True 可以发送广播
udp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, True)


# 5.发送数据                               广播地址
udp_socket.sendto("打不过我吧!".encode(), ("192.168.1.255", 8080))


# 6.关闭
udp_socket.close()
