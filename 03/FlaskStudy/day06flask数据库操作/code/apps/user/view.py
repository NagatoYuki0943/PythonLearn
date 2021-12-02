import re
from flask import Blueprint, url_for, request
from flask.templating import render_template
from werkzeug.utils import redirect
from apps.user.models import User
from exts import db
import hashlib
import json

user_bp = Blueprint('user', __name__)


@user_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        repassword = request.form.get('repassword')
        phone = request.form.get('phone')
        if password == repassword:
            # 与模型结合
            # 1. 找到模型类并创建对象
            user = User()
            # 2. 给对象的属性赋值
            user.username = username
            user.password = hashlib.sha256(password.encode('utf-8')).hexdigest()    # hexdigest() 转换为字符串
            user.phone = phone
            # 添加
            # 3.将user对象添加到session中（类似缓存）
            db.session.add(user)
            # 4.提交数据
            db.session.commit()
            return redirect(url_for('user.center')) # url_for()里面填写的是 Blueprint + func名字
        else:
            return render_template('user/register.html', msg='两次密码不同', username=username, phone=phone)

    return render_template('user/register.html')


@user_bp.route('/')
def center():   # url_for('user.center')
    # 查询所有数据 多条数据是列表,1条数据是对象
    users = User.query.all()
    # print(users) # [<User 1>, <User 2>, <User 3>, <User 4>]

    return render_template('user/center.html', users=users)


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
    return 'search'


@user_bp.route('/update')
def update():
    id = request.args.get('id')
    return 'update'


@user_bp.route('/delete')
def delete():
    id = request.args.get('id')
    return 'delete'


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

    # 4.
    User.query.filter(User.username == 'a')


    return render_template('user/test.html', user=user, user1=user1, user2=user2)