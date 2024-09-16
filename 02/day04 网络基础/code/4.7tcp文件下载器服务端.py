# 1.导入模块
import socket

# 2.创建套接字
tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 3.绑定端口
tcp_server_socket.bind(("192.168.1.103", 8081))

# 4.设置监听,套接字由主动为被动
tcp_server_socket.listen(128)


while True:
    # 5.接受客户端连接
    new_client_socket, client_ip_port = tcp_server_socket.accept()
    print(f"欢迎新客户端:{client_ip_port}")

    # 6.接收客户端发送的文件名
    file_name = new_client_socket.recv(1024).decode()
    print(file_name)

    try:
        # 7.根据文件名读取文件内容         二进制方式打开,二进制文件不能写编码
        # with open 不用close
        with open("files/" + file_name, "rb") as file:
            # 一直读取文件,知道结束
            while True:
                file_data = file.read(1024)
                if file_data:
                    # 8.把文件内容发送给客户端
                    new_client_socket.send(file_data)
                else:
                    break
    except Exception as e:
        print(f"文件:{file_name}下载失败")
    else:
        print(f"文件:{file_name}下载成功")

    # 9.关闭和当前客户端的连接
    new_client_socket.close()


# 10.关闭服务器
tcp_server_socket.close()
