'''
商品表和 User Goods 中间表
多对多关联下,一个表要想获取另一个表

用于多对多测试,不是博客的内容
'''

from exts import db

class Goods(db.Model):
    id    = db.Column(db.Integer, primary_key=True, autoincrement=True)
    gname = db.Column(db.String(100), nullable=False, comment='商品名')
    price = db.Column(db.Float, nullable=False, comment='价格')
    isdelete    = db.Column(db.Boolean, default=False, comment="软删除")

    # 这个写在主表和辅表都可以,不过只能写一个
    # 参数1:关联模型;
    # backref: 反向引用名字
    # secondary: 中间表模型 注意: UserGoods 写成 user_goods
    # 增加一个字段表示文章,不会在数据库中出现,是在模板中 关联表反向引用
    # goods.users 可以获取买了商品的用户
    # backref='goodses' 可以使用 user.goodses 反向获取商品
    users = db.relationship('User', backref='goodses', secondary='user_goods')

    def __str__(self) -> str:
        return self.gname


# User Goods 中间表
class UserGoods(db.Model):
    id       = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id  = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False, comment="用户外键")   # laravel中不使用外键即可,直接绑定就行
    goods_id = db.Column(db.Integer, db.ForeignKey('goods.id'), nullable=False, comment="商品外键")  # ForeignKey()里面是数据表的名字,必须为小写
    number   = db.Column(db.Integer, default=1, comment="购买数量")
