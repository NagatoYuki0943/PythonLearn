'''
文章控制器
'''

import re
from flask import Blueprint, request, redirect, url_for, session, g
from flask.templating import render_template
from apps.user.models import User
from apps.article.models import Article, ArticleType, Comment
from exts import db

# url_prefix前面必须有 '/'
article_bp = Blueprint('article', __name__, url_prefix='/article')


# 自定义模板过滤器
@article_bp.app_template_filter('cdecode')
def cdecode(content):
    '''
    将blob转换为文本
    '''
    return content.decode('utf-8')


# 发布文章
@article_bp.route('/publish', methods=["GET", "POST"])
def publish():
    if request.method == "GET":
        users = User.query.filter(User.isdelete==False).all()
        types = ArticleType.query.all()
        return render_template('article/publish.html', users=users, types=types)
    else:
        title = request.form.get('title')
        type_id = request.form.get('type_id')
        content = request.form.get('content')
        user_id = session.get('uid')

        # 添加文章
        article = Article()
        article.title = title
        article.type_id = type_id
        article.content = content
        article.user_id = user_id
        db.session.add(article)
        db.session.commit()
        return redirect(url_for('user.index')) # 页面中可以使用文章找用户


# 文章详情,不一定需要登录 http://127.0.0.1:5000/article/detail/20?page=1  20就是article_id  url_for('article.detail', article_id=article.id)
@article_bp.route('/detail/<article_id>')
def detail(article_id):
    article = Article.query.get(article_id)
    types = ArticleType.query.all()

    user = None
    user_id = session.get('uid', None)
    if user_id:
        user = User.query.get(user_id)
    # 单独查询评论
    page = int(request.args.get('page', 1))
    comment_pagination = Comment.query.filter(Comment.article_id==article_id, Comment.isdelete==False).order_by(-Comment.cdatetime).paginate(page=page, per_page=2)

    return render_template('article/detail.html', article=article, types=types, user=user, comment_pagination=comment_pagination)


# 喜欢
@article_bp.route('/fav')
def fav():
    article_id = request.args.get('aid')
    tag = request.args.get('tag')
    article = Article.query.get(article_id)
    # 1代表已经喜欢了,再点击就取消
    if tag == '1':
        article.fav_number -=1
    else:
        article.fav_number +=1
    db.session.commit()
    return {'code':200, 'number':article.fav_number}


# 收藏
@article_bp.route('/collect')
def collect():
    article_id = request.args.get('aid')
    tag = request.args.get('tag')
    article = Article.query.get(article_id)
    # 1代表已经收藏过了,再点击就取消
    if tag == '1':
        article.collect_number -=1
    else:
        article.collect_number +=1
    db.session.commit()
    return {'code': 200, 'number': article.collect_number}


# 发表评论,需要登录
@article_bp.route('comment', methods=['GET', 'POST'])
def comment():
    if request.method == 'POST':
        article_id = request.form.get('aid')
        comment_content = request.form.get('comment')
        user_id = g.user.id # 必须登录才能发表评论,必须通过user.view中的before_request
        # 添加到数据库
        comment = Comment()
        comment.comment = comment_content
        comment.article_id = article_id
        comment.user_id = user_id
        db.session.add(comment)
        db.session.commit()
        # 跳转需要id
        return redirect(url_for('article.detail', article_id=article_id))


# 文章分类检索
@article_bp.route('type_search')
def type_search():
    # 用户
    uid = session.get('uid')
    user = None
    if uid:
        user = User.query.get(uid)

    # 分类
    types = ArticleType.query.all()

    # 分类id获取
    tid = request.args.get('tid', 1)
    # 没用分页,因为是使用type直接获取的,要分页得手动查找
    type = ArticleType.query.get(tid)

    return render_template('article/article_type.html', user=user, types=types, type=type)
