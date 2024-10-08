from flask import Flask
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand  # 2.7版本才有MigrateCommand
from apps import create_app
from exts import db  # 导入映射的db
from apps.user.models import User  # 必须导入模型

app = create_app()

# 创建migrate,和app进行映射
migrate = Migrate(app=app, db=db)

manager = Manager(app=app)
# 将migrate命令添加到migrate
manager.add_command("db", MigrateCommand)  # 参数是名字和命令,名字是在命令行中使用


# 添加自定义命令 python app.py init
@manager.command
def init():
    print("初始化")


if __name__ == "__main__":
    # 使用manager激活 python app.py runserver
    manager.run()
