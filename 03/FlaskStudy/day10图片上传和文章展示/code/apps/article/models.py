'''
文章表
和用户表是一对多关系,文章表中有用户表的外键
'''

from sqlalchemy.orm import backref
from exts import db
from datetime import datetime


class Article(db.Model):
    '''
    文章表
    db.Text: 长文本
    '''
    id          = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title       = db.Column(db.String(50), nullable=False, comment="标题")
    content     = db.Column(db.Text, nullable=False, comment="内容")    # 数据库中改为blob,插入富文本才不会出错
    read_number = db.Column(db.Integer, default=0, comment="阅读数")
    collect_number = db.Column(db.Integer, default=0, comment="收藏数")
    fav_number  = db.Column(db.Integer, default=0, comment="喜欢数")
    user_id     = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False, comment="用户外键")
                                        # ForeignKey()里面是数据表的名字,必须为小写 ArticleType => article_type
    type_id     = db.Column(db.Integer, db.ForeignKey('article_type.id'), nullable=False, comment="文章分类外键")
    pdatetime   = db.Column(db.DateTime, default=datetime.now, comment="发布时间")
    isdelete    = db.Column(db.Boolean, default=False, comment="软删除")

    # 这个写在主表和辅表都可以,不过只能写一个
    # 参数1:关联模型;
    # backref: 反向引用名字
    # secondary: 中间表模型
    # 增加一个字段表示文章,不会在数据库中出现,是在模板中 关联表反向引用
    comments = db.relationship('Comment', backref='article')    # 只通过article找comment

    def __str__(self):
        return self.title


class Comment(db.Model):
    __tablename__ = 'comment'  # 更改表名,默认是class名字的小写
    '''
    评论表
    记录文章id和用户id 所以是多对多的关联表
    '''
    id         = db.Column(db.Integer, primary_key=True, autoincrement=True)
    comment    = db.Column(db.String(255), nullable=False, comment="评论内容")
    article_id = db.Column(db.Integer, db.ForeignKey('article.id'), comment="文章外键")
    user_id    = db.Column(db.Integer, db.ForeignKey('user.id'), comment="用户外键")
    cdatetime  = db.Column(db.DateTime, default=datetime.now, comment="评论时间")
    isdelete   = db.Column(db.Boolean, default=False, comment="软删除")

    def __str__(self):
        return self.comment


class ArticleType(db.Model):
    '''
    文章分类表

    数据库中的名字是: article_type
    '''
    id       = db.Column(db.Integer, primary_key=True, autoincrement=True)
    typename = db.Column(db.String(50), nullable=False, comment="分类名")
    isdelete = db.Column(db.Boolean, default=False, comment="软删除")

    # 关联文章表
    articles = db.relationship('Article', backref='article_type')