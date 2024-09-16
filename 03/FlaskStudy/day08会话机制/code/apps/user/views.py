"""
用户控制器
使用模板继承

ajax手机号
cookie session
"""

from operator import or_
import re
from flask import Blueprint, url_for, request, session
from flask.templating import render_template
from werkzeug.utils import redirect
from apps.user.models import User
from exts import db
from werkzeug.security import (
    generate_password_hash,
    check_password_hash,
)  # 加密,解密密码
from sqlalchemy import or_, and_, not_
from datetime import datetime, timedelta

# url_prefix 是url前缀,必须有 '/'
# 作用是 127.0.0.2:5000/user 加上自己的路由
users_bp = Blueprint(name="user", import_name=__name__, url_prefix="/user")


# 首页,获取cookie
@users_bp.route("/")
def index():
    # 1.获取cookie,也是字典格式,可以设置默认值
    # uid = request.cookies.get('uid', None)
    # 2.session方式 字典格式
    uid = session.get("uid", None)
    if uid:
        user = User.query.get(uid)
        return render_template("user/index.html", user=user)
    else:
        return render_template("user/index.html")


# ajax手机号唯一
@users_bp.route("/checkphone", methods=["GET", "POST"])
def checkphone():
    phone = request.args.get("phone")
    # 是否存在
    user = User.query.filter(User.isdelete == False, User.phone == phone).all()
    if user:
        return {"code": 1, "msg": "号码已经被注册"}
    else:
        return {"code": 0, "msg": "号码可以使用"}


# 注册
@users_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("user/register.html", user=None)  # 必需传递用户,不然报错
    else:
        username = request.form.get("username")
        password = request.form.get("password")
        repassword = request.form.get("repassword")
        phone = request.form.get("phone")
        email = request.form.get("email")
        # 与模型结合
        # 1. 找到模型类并创建对象
        user = User()
        # 2. 给对象的属性赋值
        user.username = username
        user.phone = phone
        user.email = email
        if password == repassword:
            # user.password = hashlib.sha256(password.encode('utf-8')).hexdigest()    # hexdigest() 转换为字符串

            # 密码格式 pbkdf2:sha256$salt$hash
            user.password = generate_password_hash(
                password=password, method="pbkdf2:sha256", salt_length=8
            )  # 这个方法也能加密
            # return user.password # pbkdf2:sha256:260000$0mNOkiQR$f4d7d4bfcd2059faec0a0b4274470b73981b471e40f94adba841dcf6203fd7dd
            # 添加
            # 3.将user对象添加到session中（类似缓存）
            db.session.add(user)
            # 4.提交数据
            db.session.commit()
            return redirect(
                url_for("user.index")
            )  # url_for()里面填写的是 Blueprint + func名字
        else:
            return render_template("user/register.html", msg="两次密码不同", user=user)


# 登录,添加cookie
@users_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("user/login.html")
    else:
        username = request.form.get("username")
        password = request.form.get("password")

        # 查询
        user_list = User.query.filter(username == username).all()
        # print(user_list) # 用户对象列表
        for user in user_list:
            # user就是每一个用户对象
            # 参数1: 经过加密的密码
            # 参数2: 字符串
            # return: True/False
            res = check_password_hash(pwhash=user.password, password=password)
            if res:
                # # 1.cookie
                # response = redirect(url_for('user.index'))
                # # 设置cookie
                # # key value 最大时长 默认情况是尽可能的长
                # # key,value必须为str
                # # 或者使用 expires: 过期时间 expires=datetime.now()+timedelta(hour=1)
                # response.set_cookie(key='uid', value=str(user.id), max_age=30)
                # return response

                # 2.session 字典的使用方式
                session["uid"] = user.id
                return redirect(url_for("user.index"))
        else:
            return render_template(
                "user/login.html", msg="账户或密码错误", username=username
            )


# 退出登录,删除cookie
@users_bp.route("logout")
def logout():
    response = redirect(url_for("user.index"))
    # 1.删除cookie
    # response.delete_cookie(key='uid')
    # 2.删除session
    del session["uid"]
    # session.clear()   # 清除全部session
    return response
