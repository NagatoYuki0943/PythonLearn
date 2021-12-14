'''
文章控制器
'''

from flask import Blueprint, request, redirect, url_for
from flask.templating import render_template
from apps.user.models import User
from apps.article.models import Article
from exts import db

# url_prefix前面必须有 '/'
article_bp = Blueprint('article', __name__, url_prefix='/article')


# 发布文章
@article_bp.route('/publish', methods=["GET", "POST"])
def publish():
    if request.method == "GET":
        users = User.query.filter(User.isdelete==False).all()
        return render_template('article/publish.html', users=users)
    else:
        title = request.form.get('title')
        content = request.form.get('content')
        user_id = request.form.get('user_id')   # 要有用户id
        # 添加文章
        article = Article()
        article.title = title
        article.content = content
        article.user_id = user_id
        db.session.add(article)
        db.session.commit()
        return redirect(url_for('article.all_article')) # 页面中可以使用文章找用户


# 展示所有文章
@article_bp.route('/all')
def all_article():
    articles = Article.query.filter(Article.isdelete==False).all()
    return render_template('article/all.html' , articles=articles)  # 可以通过 article.user 获取用户信息


# 展示某一个作者的所有文章 http://127.0.0.1:5000/author_all?id=2
@article_bp.route('/author_all')
def author_all():
    id = request.args.get('id')
    user = User.query.get(id)

    # User model中有文章字段,可以再前端使用 user.articles 获取所有相关文章
    # articles = db.relationship('Article', backref='user')
    return render_template('article/author_all.html', user=user)