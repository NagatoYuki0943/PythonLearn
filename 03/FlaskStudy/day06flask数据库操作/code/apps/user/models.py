# 通过 ORM 映射建立表  类 ----》 表
'''
在 app.py中导入这两个类
python app.py db init       产生一个文件夹migrations 只需要init一次
python app.py db migrate    自动产生了一个版本文件,添加数据表Model就使用一次
python app.py db upgrade    新建(更新数据表)
python app.py db downgrade  降级(回到上一个数据表)
注意: 上面的db是在app.py中添加进去的
    # 将migrate命令添加到migrate
    manager.add_command('db', MigrateCommand)   # 参数是名字和命令
'''
from exts import db
from datetime import datetime


# create table user(id int primarykey auto_increment,username varchar(20) not null,..)
class User(db.Model):
    '''
    不用在__init__中写,在类全局写
    列: db.Column(类型，约束)  映射表中的列
    类型：
    db.Integer      int
    db.String(15)   varchar(15)
    db.Datetime     datetime
    db.Boolean
    '''
    id        = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username  = db.Column(db.String(15), nullable=False)
    password  = db.Column(db.String(256), nullable=False)
    phone     = db.Column(db.String(11), unique=True)
    email     = db.Column(db.String(20))
    realname  = db.Column(db.String(20), comment="真实姓名") # comment是字段说明,自己试出来的
    isdelete  = db.Column(db.Boolean, default=False)
    rdatetime = db.Column(db.DateTime, default=datetime.now)

    def __str__(self):
        return self.username

