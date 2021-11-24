"""
render_template('相对于templates下的路径')

GET 返回字典
request.args
request.args.get('username')

POST 返回字典
request.form
request.form.get('username')

"""

from flask import Flask, request, render_template

import settings

app = Flask(__name__)
app.config.from_object(settings)


@app.route('/')
def register():
    return render_template('register6.html')   # 默认去模板文件夹中找文件夹的


@app.route('/response', methods=['GET', 'POST'])
def response():  # 获取页面提交的内容
    print(request.full_path)                # GET: /response?username=admin&password=123456   POST: /response?
    print(request.path)                     # /response

    # get 返回字典
    print(request.args)                     # ImmutableMultiDict([('username', 'admin'), ('address', '123456')])
    # 使用get在数据不存在时不会报错,使用字典直接获取会报错
    print(request.args.get('username'))     # admin
    print(request.args.get('password'))     # 123456
    print(request.args['password'])         # 123456
    print('*' * 50)

    # post 返回字典
    # 使用get在数据不存在时不会报错,使用字典直接获取会报错
    print(request.form)                     # ImmutableMultiDict([('username', 'admin'), ('address', '123456')])
    print(request.form.get('username'))     # admin
    print(request.form['password'])         # 123456
    return '进来了'


if __name__ == '__main__':
    print(app.url_map)  # 路由规则表
    print('*' * 50)
    app.run()
