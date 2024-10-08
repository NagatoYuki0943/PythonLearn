"""
if使用
    {% if i %}
    {% else %}
    {% endif %}
for循环和循环
{% for i in girls %}
    {{ i }}
{% endfor %}

loop使用  {{}} {%%} 都可以使用
    {% for i in girls %}
    loop.length
    loop.index
    loop.index0
    loop.revindex
    loop.revindex
    loop.first
    loop.last
{% endfor %}
"""

from flask import Flask, render_template

import settings

app = Flask(__name__)

app.config.from_object(settings)


@app.route("/")
def show1():
    girls = ["如花", "凤姐", "宋宋", "孙艺珍", "建玲", "林允儿"]
    users = [
        {
            "username": "zhangsan1",
            "password": "123123",
            "addr": "北京",
            "phone": "13900001010",
        },
        {
            "username": "zhangsan2",
            "password": "123111",
            "addr": "上海",
            "phone": "13900991010",
        },
        {
            "username": "zhangsan3",
            "password": "123222",
            "addr": "武汉",
            "phone": "13900009990",
        },
        {
            "username": "zhangsan4",
            "password": "123333",
            "addr": "西安",
            "phone": "13900008810",
        },
        {
            "username": "zhangsan5",
            "password": "123444",
            "addr": "成都",
            "phone": "13977771010",
        },
        {
            "username": "zhangsan6",
            "password": "123555",
            "addr": "深圳",
            "phone": "13900121010",
        },
    ]
    return render_template("2_show.html", girls=girls, users=users)


if __name__ == "__main__":
    app.run()
