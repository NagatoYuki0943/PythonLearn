from flask import Flask
# 导入路径是相对于外面的app.py来说的
import settings
from apps.user.view import user_bp
import sys


def create_app():
    app = Flask(__name__,
                template_folder='../templates',      # 要定义templates和static文件夹位置,因为默认是在__init__同级别
                static_folder='../static')

    # 这个执行路径的确是上一层目录,不过Flask认为是当前目录,应该是实例化的目录
    # print(sys.path[0])
    # d:\Python\Pycharm\03\FlaskStudy\day04flask模板复用\code\综合案例

    app.config.from_object(settings)    # 导入配置文件
    app.register_blueprint(user_bp)     # 注册蓝图 里面的路由就直接用就可以,不需要加url前缀
    return app


if __name__ == '__main__':
    create_app()