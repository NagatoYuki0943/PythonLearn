"""
自定义过滤器 在html中的语法和自带过滤器相同
app.add_template_filter(函数名, '名字')
@app.template_filter('名字')
"""

from flask import Flask, render_template

import settings

app = Flask(__name__)
app.config.from_object(settings)


@app.route("/")
def hello_world():
    msg = "hello everyone hello world"
    li = [3, 7, 9, 1, 5]
    return render_template("4_define_filter.html", msg=msg, li=li)


# 过滤器本质就是函数
# 第一种方式
def replace_hello(value: str):
    print("------>", value)
    value = value.replace("hello", "")
    print("======>", value)
    return value.strip()  # 将 替换的结果返回


app.add_template_filter(replace_hello, "replace")


# 第二种方式 装饰器
@app.template_filter("listreverse")
def reverse_list(li: list):
    temp_li = list(li)
    temp_li.reverse()
    return temp_li


if __name__ == "__main__":
    app.run()
