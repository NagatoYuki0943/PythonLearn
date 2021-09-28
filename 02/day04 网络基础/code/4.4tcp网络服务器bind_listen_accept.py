'''
要绑定ip和端口,让别人来访问
tcp_server_socket.bind(('192.168.1.103', 8081))

开启监听(设置套接字为别动模式)
最大允许128个连接,在windows 128 有效,在linux下无效
tcp_server_socket.listen(128)

允许连接,accept() 会进入阻塞状态,有连接才继续
返回值分为两部分: 第一部分是新的套接字,第二部分是客户端ip和端口号
新套接字只服务于目前的客户端

# socket.SO_REUSEADDR 代表地址是否可以重用, 参数3写True:可以重用; False:不能重用
tcp_server_socket = socket.socket(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)

'''

# 1.导入模块
import socket


# 2.创建套接字
tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# socket.SO_REUSEADDR 代表地址是否可以重用, 参数3写True:可以重用; False:不能重用
# tcp_server_socket = socket.socket(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)



# 3.绑定ip和端口
tcp_server_socket.bind(('192.168.1.103', 8081))


# 4.开启监听(设置套接字为别动模式)
# 最大允许128个连接,在windows 128 有效,在linux下无效
tcp_server_socket.listen(128)


# 5.等待客户端连接,accept() 会进入阻塞状态,有连接才继续
# 返回值分为两部分: 第一部分是新的套接字,第二部分是客户端ip和端口号
# 新套接字只服务于目前的客户端
new_client_socket,client_ip_port = tcp_server_socket.accept()
print('新客户端上线了')
print(new_client_socket)    # <socket.socket fd=376, fam...>
print(client_ip_port)       # ('192.168.1.103', 59175)


# 6.使用新的套接字收发数据
new_client_socket.send('哈哈哈哈哈\n'.encode())
data = new_client_socket.recv(1024)
print(data.decode('gbk'))


# 7. 关闭连接
# 不能再和当前的客户端通信
new_client_socket.close()
# 关闭服务器,不再接收新的客户端,已经连接的继续提供服务
tcp_server_socket.close()