from flask_migrate import Migrate
from apps import create_app
from exts import db                 # 导入映射的db
from apps.user.models import *      # 必须导入模型
from apps.article.models import *

app = create_app()

# 创建migrate,和app进行映射
migrate = Migrate(app=app, db=db)


if __name__ == '__main__':
    app.run()
