'''
商品控制器
'''

from flask import Blueprint, request, redirect, url_for
from flask.templating import render_template
from apps.user.models import User
from apps.goods.models import Goods
from apps.article.models import Article
from apps.goods.models import UserGoods
from exts import db


goods_bp = Blueprint('goods', __name__)


# 用户买商品
@goods_bp.route('/show')
def show():
    users = User.query.filter(User.isdelete==False).all()
    goodses = Goods.query.filter(Goods.isdelete==False).all()
    return render_template('goods/show.html', users=users, goodses=goodses)


# 买商品
@goods_bp.route('/buy')
def buy():
    user_id = request.args.get('user_id')
    goods_id =request.args.get('goods_id')
    user_goods = UserGoods()
    user_goods.user_id = user_id
    user_goods.goods_id = goods_id
    db.session.add(user_goods)
    db.session.commit()
    return '购买成功'


# 用户找买了的商品
@goods_bp.route('/findgoods')
def findgoods():
    pass


# 根据商品找买的用户
@goods_bp.route('/finduser')
def finduser():
    pass


