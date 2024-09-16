# 通过 ORM 映射建立表  类 ----》 表
"""
在 app.py中导入这两个类
python app.py db init       产生一个文件夹migrations 只需要init一次
python app.py db migrate    自动产生了一个版本文件,添加数据表Model就使用一次
python app.py db upgrade    新建(更新数据表)
python app.py db downgrade  降级(回到上一个数据表)
注意: 上面的db是在app.py中添加进去的
    # 将migrate命令添加到migrate
    manager.add_command('db', MigrateCommand)   # 参数是名字和命令
"""

from exts import db
from datetime import date, datetime


# create table user(id int primarykey auto_increment,username varchar(20) not null,..)
class User(db.Model):
    """
    用户表
    不用在__init__中写,在类全局写
    列: db.Column(类型，约束)  映射表中的列
    类型:
    db.Integer      int
    db.String(15)   varchar(15)
    db.Datetime     datetime
    db.Boolean
    """

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(256), nullable=False, comment="用户名")
    password = db.Column(db.String(1024), nullable=False, comment="密码")
    phone = db.Column(db.String(20), unique=True, nullable=True, comment="手机")
    email = db.Column(db.String(50), comment="email")
    icon = db.Column(db.String(256), comment="头像")
    realname = db.Column(
        db.String(50), comment="真实姓名"
    )  # comment是字段说明,自己试出来的
    isdelete = db.Column(db.Boolean, default=False, comment="软删除")
    rdatetime = db.Column(db.DateTime, default=datetime.now, comment="注册时间")

    # 这个写在主表和辅表都可以,不过只能写一个
    # 参数1:关联模型;
    # backref: 反向引用名字
    # secondary: 中间表模型
    # 增加一个字段表示文章,不会在数据库中出现,是在模板中 关联表反向引用
    # user.articles 可以获取相关文章列表
    # backref='user' 可以使用 article.user 反向获取用户
    articles = db.relationship("Article", backref="user")
    # 这个人发表的评论有哪些
    comments = db.relationship("Comment", backref="user")

    def __str__(self):
        return self.username


class Photo(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(
        db.String(1024), nullable=False, comment="图片名字,实际存放的是本地路径"
    )
    user_id = db.Column(
        db.Integer, db.ForeignKey("user.id"), nullable=False, comment="用户id"
    )
    isdelete = db.Column(db.Boolean, default=False, comment="软删除")
    pdatetime = db.Column(db.DateTime, default=datetime.now, comment="上传时间")

    def __str__(self) -> str:
        return self.name
