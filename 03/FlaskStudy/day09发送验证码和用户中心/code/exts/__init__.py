# 创建一个映射对象,映射到数据库
from flask_sqlalchemy import SQLAlchemy

# boostrap
from flask_bootstrap import Bootstrap

db = SQLAlchemy()
bootstrap = Bootstrap()
