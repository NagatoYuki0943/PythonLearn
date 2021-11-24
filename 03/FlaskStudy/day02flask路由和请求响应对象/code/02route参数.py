from flask import Flask
import settings

app = Flask(__name__)
app.config.from_object(settings)


@app.route('/')
def index():
    return 'index'


city_data = {'a': '北京', 'b': '上海', 'c': '深圳'}


# <变量>,函数名也得写
@app.route('/city/<key>')
def city(key: str):
    print(type(key))
    return city_data[key]
    # http://127.0.0.1:5000/city/b 上海


@app.route('/add/<int:a>')
def add(a: int):
    print(type(a))
    return str(a + 10)  # 返回值要设置为str
    # http://127.0.0.1:5000/add/10 20


@app.route('/add1/<float:money>')   # 必须是float,不能是int
def add1(money: float):
    print(type(money))
    return str(money)


@app.route('/index/<path:p>')
def get_path(p):
    print('******>', type(p))  # str类型
    print(p)
    return p


@app.route('/test/<uuid:uid>')  # 必须传递uuid的格式，uuid模块， uuid.uuid4() ---->UUID类型
def test(uid):
    print('#######>>>>>', type(uid))
    return '获取唯一的标识码'


# url多个变量
@app.route('/add2/<int:a>/<int:b>')
def add2(a: int, b: int):
    return str(a + b)
    # http://127.0.0.1:5000/add2/1/2  3


if __name__ == '__main__':

    app.run()
