'''
用户控制器
'''

from operator import or_
import re
from flask import Blueprint, url_for, request
from flask.templating import render_template
from werkzeug.utils import redirect
from apps.user.models import User
from exts import db
import hashlib
from sqlalchemy import or_, and_, not_
import json

user_bp = Blueprint('user', __name__)


@user_bp.route('/')
def center():   # url_for('user.center')
    # 查询没有删除的数据 多条数据是列表,1条数据是对象
    users = User.query.filter(User.isdelete == False).all()
    # print(users) # [<User 1>, <User 2>, <User 3>, <User 4>]

    return render_template('user/center.html', users=users)


@user_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('user/register.html', user=None) # 必需传递用户,不然报错
    else:
        username = request.form.get('username')
        password = request.form.get('password')
        repassword = request.form.get('repassword')
        phone = request.form.get('phone')
        # 与模型结合
        # 1. 找到模型类并创建对象
        user = User()
        # 2. 给对象的属性赋值
        user.username = username
        user.phone = phone
        if password == repassword:
            user.password = hashlib.sha256(password.encode('utf-8')).hexdigest()    # hexdigest() 转换为字符串
            # 添加
            # 3.将user对象添加到session中（类似缓存）
            db.session.add(user)
            # 4.提交数据
            db.session.commit()
            return redirect(url_for('user.center')) # url_for()里面填写的是 Blueprint + func名字
        else:
            return render_template('user/register.html', msg='两次密码不同', user=user)


@user_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        new_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
        # 查询
        user_list = User.query.filter_by(username=username) # filter_by 相当于where
        # print(user_list) # 用户对象列表
        for user in user_list:
            # user就是每一个用户对象
            if user.password == new_password:
                return "用户登录成功"
        else:
            return render_template('user/login.html', msg="账户或密码错误", username=username)

    return render_template('user/login.html')


@user_bp.route('/search')
def search():
    '''
    通过用户名或手机号查询
    '''
    keyword = request.args.get('search')
    users = User.query.filter(User.isdelete == False).filter(or_(User.username.contains(keyword), User.phone.contains(keyword))).all()
    # 返回给center
    return render_template('user/center.html', users=users)


@user_bp.route('/update', methods=['GET', 'POST'])
def update():
    if request.method == 'GET':
        id = request.args.get('id')
        user = User.query.get(id)
        return render_template('user/update.html', user=user)
    else:
        id = request.form.get('id')
        username = request.form.get('username')
        password = request.form.get('password')
        repassword = request.form.get('repassword')
        phone = request.form.get('phone')
        # 1. 找到对象
        user = User.query.get(id)
        # 2. 给对象更新属性
        user.username = username
        user.phone = phone
        if password == repassword:
            # 与模型结合
            user.password = hashlib.sha256(password.encode('utf-8')).hexdigest()    # hexdigest() 转换为字符串
            # 3.提交数据
            db.session.commit()
            return redirect(url_for('user.center'))
        else:
            return render_template('user/update.html', msg='两次密码不同', user=user)


@user_bp.route('/delete')
def delete():
    id = request.args.get('id')
    user = User.query.get(id)

    # 1.逻辑删除
    user.isdelete = True
    # 提交
    db.session.commit()

    # 2.真实删除
    # db.session.delete(user)
    # db.session.commit()
    return redirect(url_for('user.center'))


@user_bp.route('/test')
def test():
    username = request.args.get('username')

    # 1.first()返回第一个对象
    user = User.query.filter_by(username=username).first()
    # print(user) # a

    # 2.根据id获取对象
    user = User.query.get(1)

    # 3.filter里面填写 ==, filter_by里面填写 =
    user1 = User.query.filter(User.username == 'a').all()   # 对象列表
    user2 = User.query.filter(User.username == 'a').first() # 对象

    # 4.复杂使用
    User.query.filter(User.username == 'a')

    '''
    # 返回对象列表
    User.query.filter(User.username.startswith('z')).all() # 开始 select * from user where username like 'z%';
    User.query.filter(User.username.endswith('z')).all()   # 结束 select * from user where username like '%z';
    User.query.filter(User.username.contains('z')).all()   # 包含 select * from user where username like '%z%';
    User.query.filter(User.username.like('z%')).all()	   # 像
    User.query.filter(User.username.ilike('z%')).all()	   # 像 忽略大小写
    User.query.filter(User.username.notlike('z%')).all()   # 不像
    User.query.filter(User.username.notilike('z%')).all()  # 不像 忽略大小写
    User.query.filter(User.age > 8).all()
    # 找到一个对象
    User.query.filter(User.age > 8).first()
    '''

    '''
    并且： and_    或者： or_   非： not_

    User.query.filter(and_(User.username.contains('i'), User.rdatetime.__gt__('2020-05-25 10:30:00'))).all()
    User.query.filter(and_(User.username.contains('i'), User.rdatetime >'2020-05-25 10:30:00')).all()
    # select * from user where username like '%i%' and rdatetime < 'xxxx'

    User.query.filter(or_(User.username.like('z%'), User.username.contains('i'))).all()
    # 类似： select * from user where username like 'z%' or username like '%i%';

    __gt__,__lt__,__ge__(gt equal),__le__ (le equal)  也可以直接使用 >  <  >=  <=  !=
    '''

    '''
    in 在...之中
    User.query.filter(User.phone.in_([17, 17, 20, 22])).all()
    select * from user where age in [17, 18, 20, 22];
    '''

    '''
    between(start, end)
    User.query.filter(User.phone.between(20, 22)).all()
    '''

    '''
    order_by 排序 默认升序
    user_list = User.query.filter(User.username.contains('z')).order_by(User.rdatetime).all()   # 先筛选再排序
    user_list = User.query.filter(User.username.contains('z')).order_by('rdatetime').all()      # 先筛选再排序
    user_list = User.query.order_by(User.id).all()  # 对所有的进行排序

    降序
    user_list = User.query.order_by(-User.id).all() # 降序
    '''

    '''
    limit offset
    user_list = User.query.limit(2).all()             # 默认获取前两条
    user_list = User.query.offset(2).limit(2).all()   # 跳过2条记录再获取两条记录
    '''

    return render_template('user/test.html', user=user, user1=user1, user2=user2)