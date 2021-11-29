"""
redirect('url')  重定向
url_for('route中的endpoint') 反向路由解析
"""

import json

from flask import Flask, render_template, request, redirect, url_for

import settings

app = Flask(__name__)
app.config.from_object(settings)

users = []


@app.route('/', endpoint='index')   # endpoint
def index():
    return render_template('index.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        repassword = request.form.get('repassword')
        if password == repassword:
            user = {'username': username, 'password':password}
            users.append(user)

            # 重定向,跳转网页
            return redirect(url_for('index'))   # url_for参数是endpoint,返回的url路径
        else:
            return "<h1>两次密码不一致</h1>"
    return render_template('register7.html')


@app.route('/show')
def show():
    # json字符串
    j_str = json.dumps(users)
    return j_str    # [{"username": "a", "password": "12"}, {"username": "b", "password": "1"}]


@app.route('/test')
def test():
    url = url_for('index')  # 路径反向解析, 参数是endpoint,返回的url路径
    print(url)  # /
    return redirect(url)


if __name__ == '__main__':
    app.run(port=5001)
