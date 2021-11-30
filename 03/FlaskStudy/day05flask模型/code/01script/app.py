from flask import Flask
from flask_script import Manager

from apps import create_app

app = create_app()

manager = Manager(app=app)

# 添加自定义命令 python app.py init
@manager.command
def init():
    print('初始化')


if __name__ == '__main__':
    # 使用manager激活 python app.py runserver
    manager.run()
