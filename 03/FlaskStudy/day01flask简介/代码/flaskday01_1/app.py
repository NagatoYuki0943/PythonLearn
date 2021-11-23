from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!hello kitty!~~~~'


if __name__ == '__main__':
    # ip, 端口, debug模式
    app.run(host='0.0.0.0', port=5001, debug=True)
