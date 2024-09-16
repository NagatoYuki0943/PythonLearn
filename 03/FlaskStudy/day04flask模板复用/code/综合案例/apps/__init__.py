from flask import Flask

# 导入路径是相对于外面的app.py来说的
import settings
from apps.user.view import user_bp


def create_app():
    app = Flask(
        __name__,
        template_folder="../templates",  # 要定义templates和static文件夹位置,因为默认是在__init__同级别
        static_folder="../static",
    )  # 这两个路径和参数1:import_name就是`__name__`相关,是根据它来确定自己的相对路径

    app.config.from_object(settings)  # 导入配置文件
    app.register_blueprint(user_bp)  # 注册蓝图 里面的路由就直接用就可以,不需要加url前缀
    return app


if __name__ == "__main__":
    create_app()
