'''
商品控制器
用于多对多测试,不是博客的内容
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
    # 添加到中间表
    user_goods = UserGoods()
    user_goods.user_id = user_id
    user_goods.goods_id = goods_id
    db.session.add(user_goods)
    db.session.commit()
    return '购买成功'


# 根据商品找买的用户
@goods_bp.route('/finduser')
def finduser():
    # 商品id
    goods_id = request.args.get('goods_id')
    goods = Goods.query.get(goods_id)

    # Goods表中 users = db.relationship('User', backref='goodses', secondary='user_goods') secondary是中间表
    # 在html中可以使用 goods.users 获取所有买了产品的用户
    return render_template('goods/finduser.html' , goods=goods)


# 用户找买了的商品
@goods_bp.route('/findgoods')
def findgoods():
    id = request.args.get('user_id')
    user = User.query.get(id)
    # Goods表中 users = db.relationship('User', backref='goodses', secondary='user_goods') secondary是中间表
    # 在html中可以使用 user.goodsed 获取所有买的商品
    return render_template('goods/findgoods.html', user=user)