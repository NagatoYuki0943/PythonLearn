from flask import Flask, request, render_template

import settings

app = Flask(__name__)
app.config.from_object(settings)


class Girl:
    def __init__(self, name, addr):
        self.name = name
        self.gender = '女'
        self.addr = addr

    def __str__(self):
        return self.name


@app.route('/')
def show():
    name = '沈凯'  # str
    age = 18  # int
    friends = ['小明', '小红', 'Tom', 'Jerry']  # list
    dict1 = {'gift0': '止痛药', 'gift1': '安眠药', 'gift2': '麻醉剂'}  # dict
    # 创建对象
    girlfriend = Girl('叶子', '地狱')
    return render_template('1_show.html', name=name, age=age, gender='futa', friends=friends, dict1=dict1, girl=girlfriend)


if __name__ == '__main__':
    app.run()
