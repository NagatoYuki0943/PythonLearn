"""
使用蓝图绑定路由,这些路由是只针对自己的,要在__init__的app中注册蓝图
路由不用加蓝图前缀,和普通使用相同
"""

from flask import Blueprint, request, render_template, redirect
from apps.user.model import User
import json

# 创建蓝图,就是一个逻辑中枢
user_bp = Blueprint('user', __name__)

# 用户对象
users = []


# http://127.0.0.1:5000/
@user_bp.route('/')
def center():
    return render_template('user/show.html', users=users)     # 路径在 templates/user/show


# http://127.0.0.1:5000/register
@user_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # 获取数据
        username = request.form.get('username')
        password = request.form.get('password')
        repassword = request.form.get('repassword')
        phone = request.form.get('phone')
        if password == repassword:
            # 用户名是否存在
            for user in users:
                if user.username == username:
                    return render_template('user/register.html', msg="用户名已存在")

            user = User(username, password, phone)
            users.append(user)
            return redirect('/')

    return render_template('user/register.html')


# http://127.0.0.1:5000/login
@user_bp.route('/login', methods=['GET', 'POST'])
def login():
    return 'login'
    return render_template('user/login.html')


# http://127.0.0.1:5000/logout
@user_bp.route('/logout', methods=['GET', 'POST'])
def logout():
    return "用户退出"


# http://127.0.0.1:5000/delete
@user_bp.route('/delete')
def delete():
    username = request.args.get('username')
    for user in users:
        if user.username == username:
            users.remove(user)  # del不管用
            break
    return redirect('/')
