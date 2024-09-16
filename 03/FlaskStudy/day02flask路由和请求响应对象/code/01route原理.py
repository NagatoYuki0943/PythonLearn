"""
@app.route() 相当于自动调用 app.add_url_rule('url', view_func=函数名)
"""

from flask import Flask
import settings

app = Flask(__name__)
app.config.from_object(settings)


@app.route("/")
def hello_world():
    return "Hello World!"


# add_url_rule就是上面装饰器的作用
def index():
    return "welcome everyone！"


#                                  函数
app.add_url_rule("/index", view_func=index)

if __name__ == "__main__":
    app.run()
