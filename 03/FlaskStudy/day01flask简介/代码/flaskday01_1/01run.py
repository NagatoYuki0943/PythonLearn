# print(__name__)
from flask import Flask

app = Flask(__name__)


# 装饰器
@app.route('/')   # 路由  URL  http://127.0.0.1:5000/
def index():  # 视图函数   mtv： view 视图   函数
    return '哈哈哈哈哈哈'


# WSGI: Python Web Server Gateway Interface  是为Python语言定义的Web服务器和Web应用程序或框架之间的一种简单而通用的接口
if __name__ == '__main__':
    # 这样设置要手动执行才管用 python .\day01flask简介\代码\flaskday01_1\01run.py
    # ip, 端口, debug模式
    # 0.0.0.0 允许外网访问
    app.run(host='0.0.0.0', port=5001, debug=True)
# flask 内置服务器   nginx

# pip install flask
