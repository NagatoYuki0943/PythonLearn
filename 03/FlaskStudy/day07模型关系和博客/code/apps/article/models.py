'''
文章表
'''

from exts import db
from datetime import datetime


class Article(db.Model):
    '''
    db.Text: 长文本
    '''
    id          = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title       = db.Column(db.String(50), nullable=False, comment="标题")
    content     = db.Column(db.Text, nullable=False, comment="内容")
    pdatetime   = db.Column(db.DateTime, default=datetime.now, comment="发布时间")
    read_number = db.Column(db.Integer, default=0, comment="阅读数")
    collect_number = db.Column(db.Integer, default=0, comment="收藏数")
    fav_number  = db.Column(db.Integer, default=0, comment="喜欢数")
    user_id     = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False,comment="用户外键")
    isdelete    = db.Column(db.Boolean, default=False, comment="软删除")

    def __str__(self):
        return self.title