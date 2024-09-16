from flask import Flask

import settings
from apps.user.view import user_bp
from apps.user.views import user_bp
from apps.article.view import article_bp
from exts import db, bootstrap  # 导入映射的db,bootstrap


def create_app():
    app = Flask(
        __name__,
        template_folder="../templates",  # 要定义templates和static文件夹位置,因为默认是在__init__同级别
        static_folder="../static",
    )  # 这两个路径和参数1:import_name就是`__name__`相关,是根据它来确定自己的相对路径

    app.config.from_object(settings.Config)  # 导入配置文件
    # app.register_blueprint(user_bp)         # 注册蓝图 里面的路由就直接用就可以,不需要加url前缀
    app.register_blueprint(user_bp)
    app.register_blueprint(article_bp)
    db.init_app(app)  # 将db对象与app进行了关联
    bootstrap.init_app(app)  # 初始化bootstrap
    return app
