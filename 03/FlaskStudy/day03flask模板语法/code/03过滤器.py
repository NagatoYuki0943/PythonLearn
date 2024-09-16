from flask import Flask, request, render_template

import settings

app = Flask(__name__)

app.config.from_object(settings)


@app.route("/")
def show1():
    girls = ["如花", "凤姐", "宋宋", "孙艺珍", "建玲", "林允儿"]
    user = {
        "username": "小黑",
        "password": "123123",
        "addr": "北京",
        "phone": "13900001010",
    }
    msg = "<h1>520快乐！</h1>"
    n1 = "Hello"
    return render_template("3_show.html", girls=girls, user=user, msg=msg, n1=n1)


if __name__ == "__main__":
    app.run()
