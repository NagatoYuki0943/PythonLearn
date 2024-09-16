"""
外置配置
"""

from flask import Flask
import settings

app = Flask(__name__)
# 获取配置文件
app.config.from_object(settings)
print(app.config)


@app.route("/")
def index():
    return "index"


@app.route("/hell0")
def hell0():
    return "hell0"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
