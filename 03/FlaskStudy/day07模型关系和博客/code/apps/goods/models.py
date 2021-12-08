'''
商品表
'''

from exts import db

class Goods(db.Model):
    id    = db.Column(db.Integer, primary_key=True, autoincrement=True)
    gname = db.Column(db.String(100), nullable=False, comment='商品名')
    price = db.Column(db.Float, nullable=False, comment='价格')
    isdelete    = db.Column(db.Boolean, default=False, comment="软删除")

    def __str__(self) -> str:
        return self.gname


# User Goods 中间表
class UserGoods(db.Model):
    id       = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id  = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False, comment="用户外键")        # laravel中不使用外键即可,直接绑定就行
    goods_id = db.Column(db.Integer, db.ForeignKey('goods.id'), nullable=False, comment="商品外键")
    number   = db.Column(db.Integer, default=1, comment="购买数量")
