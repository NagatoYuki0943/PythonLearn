'''
文章控制器
'''

from flask import Blueprint, request, redirect, url_for, session
from flask.templating import render_template
from apps.user.models import User
from apps.article.models import Article, ArticleType
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
        return render_template('article/publish.html', users=users)
    else:
        title = request.form.get('title')
        type_id = request.form.get('type')
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


# 文章详情
@article_bp.route('/detail')
def detail():
    article_id = request.args.get('aid')
    article = Article.query.get(article_id)
    types = ArticleType.query.all()

    user = None
    user_id = session.get('uid')
    if user_id:
        user = User.query.get(user_id)

    return render_template('article/detail.html', article=article, types=types, user=user)


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
    return {'code':200, 'number':article.collect_number}


@article_bp.route('comment', methods=['GET', 'POST'])
def comment():
    return 'comment'