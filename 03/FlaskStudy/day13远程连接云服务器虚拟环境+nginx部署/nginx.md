# Nginx控制

启动Nginx

```
nginx  [ -c configpath]  默认配置目录：/etc/nginx/nginx.conf
```

信息查看

```
nginx  -v

nginx -V
```

查看进程：

```
ps -ef |grep nginx
```

控制Nginx

```
nginx -s signal

stop  快速关闭

quit 优雅的关闭

reload 重新加载配置
```

通过系统管理

```
systemctl status nginx  # 查看nginx状态

systemctl start nginx   # 启动nginx服务

systemctl stop nginx    # 关闭nginx服务

systemctl enable nginx  # 设置开机自启

systemctl disable nginx # 禁止开机自启
```

# Nginx配置文件

Nginx配置文件包含指定指令控制的模块。

 指令分为简单指令和块指令

 一个简单指令由名称和参数组成，以空格分隔，并以分号结尾

 一个块指令和简单指令具有相同的结构，但不是以分号结束，而是以一个大括号包围的一堆附 加指令结束

 如果一个大括号内可以有其他的指令，它就被称为一个上下文，比如（events，http，server，location）

 

指令

```
nginx -t 	不运行，仅测试配置文件

nginx -c   	configpath 从指定路径加载配置文件

nginx -t-c  configpath 测试指定配置文件
```

## Nginx配置文件结构

```
main		全局设置

events{		工作模式，连接配置
	...
}
http{		http的配置
	...
	upstream xxx{	负载均衡配置
		...
	}
	server{		主机设置
		...
		location xxx{	URL匹配
			...
		}
	}
}
```

### main

```
user nginx;				worker进程运行的用户和组

worker_processes 1;		指定Nginx开启的子进程数，多核CPU建议设置和CPU数量一样的进程数

error_log xxx level;	用来定义全局错误日志文件，通常放在var中，level有 debug，info，notice，warn，error，crit

pid xxx;				指定进程id的存储文件位置
```

### events

指定工作模式和以及连接上限

```
events{
	use epoll;
	worker_connections 1024;
}
```

use 指定nginx工作模式

- epoll 高效工作模式，linux
- kqueue 高效工作模式， bsd
- poll 标准模式
- select 标准模式

worker_connections 定义nginx每个进程的最大连接数

- 正向代理 连接数 * 进程数
- 反向代理 连接数 * 进程数 / 4
- linux系统限制最多能同时打开65535个文件，默认上限就是65535，可解除 ulimit -n 65535

### http

最核心的模块，主要负责http服务器相关配置，包含server，upstream子模块

```
include mime.types;	设置文件的mime类型

include xxxconfig;	包含其它配置文件，分开规划解耦

default_type  xxx;	设置默认类型为二进制流，文件类型未知时就会使用默认

log_format 			设置日志格式

sendfile			设置高效文件传输模式

keepalive_timeout	设置客户端连接活跃超时

gzip	 			gzip压缩
```

### server

用来指定虚拟主机

```
listen 	80;						指定虚拟主机监听的端口

server_name localhost;			指定ip地址或域名，多个域名使用空格隔开

charset utf-8;					指定网页的默认编码格式

error_page 500 502 /50x.html 	指定错误页面

access_log xxx main;			指定虚拟主机的访问日志存放路径

error_log xxx main;				指定虚拟主机的错误日志存放路径

root xxx;						指定这个虚拟主机的根目录

index xxx;						指定默认首页
```

### location

核心中的核心，以后的主要配置都在这

主要功能:定位url，解析url，支持正则匹配，还能支持条件，实现动静分离

> 语法

```
location [modifier]  uri{
	...
}
```

> modifier 修饰符

- =	使用精确匹配并且终止搜索
- ~	区分大小写的正则表达式
- ~*	不区分大小写的正则表达式
- ^~	最佳匹配，不是正则匹配，通常用来匹配目录

> 常用指令

- alias 别名，定义location的其他名字，在文件系统中能够找到，如果location指定了正则表达式，alias将会引用正则表达式中的捕获，alias替代lication中匹配的部分，没有匹配的部分将会在文件系统中搜索

### Django项目部署

> django 服务器 

```
runserver
wsgi
```

> uwsgi : web服务器,多线程处理的不错

1. pip install uwsgi
2. 工程目录下创建uwsgi.ini 配置文件
3. 书写配置信息
4. 使用uwsgi服务器
   - 启动 `uwsgi --ini uwsgi.ini`
   - 停止 `uwsgi -stop uwsgi.pid`

nginx配置

```
location /static{
	alias  xxx/static/;
}
location / {
	include uwsgi_params;
	uwsgi_pass localhost:8000;
}
```

### 反向代理

```
proxy_pass  URL;					反向代理转发地址，默认不转发header，需要转发header则设置proxy_set_header HOST $host;

proxy_method  POST;					转发的方法名

proxy_hide_header Cache-Control;	指定头部不被转发		

proxy_pass_header Cache-Control;	设置哪些头部转发

proxy_pass_request_header on;		设置转发http请求头

proxy_pass_request_body on;			设置转发请求体
```

### upstream

> 负载均衡模块，通过一个简单的调度算法来实现客户ip到后端服务器的负载平衡

写法

```
upstream  myproject{
	ip_hash;
    server 127.0.0.1:8000;
	server 127.0.0.1:8001 down;
	server 127.0.0.1:8002 weight=3;
	server 127.0.0.1:8003 backup；
	fair；
}
```

负载均衡算法

```
weight 	负载权重
down	当前server不参与负载均衡
backup	其它机器全down掉或满载使用此服务
ip_hash	按每个请求的hash结果分配
fair	按后端响应时间来分（第三方的）
```

