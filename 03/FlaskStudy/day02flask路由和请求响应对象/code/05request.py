"""
request直接导入即可
"""


from flask import Flask, request

import settings

app = Flask(__name__)
app.config.from_object(settings)


@app.route('/')
def index():
    # make_response()
    print("headers:\n", request.headers)  # request对象 对象访问属性，也可以调用方法
    #  Host: 127.0.0.1:5000
    # User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0
    # Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
    # Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
    # Accept-Encoding: gzip, deflate
    # Dnt: 1
    # Connection: keep-alive
    # Cookie: name="\347\277\224\345\256\207"
    # Upgrade-Insecure-Requests: 1
    # Sec-Fetch-Dest: document
    # Sec-Fetch-Mode: navigate
    # Sec-Fetch-Site: none
    # Sec-Fetch-User: ?1
    print("path:\n", request.path)
    # /
    print("full_path:\n", request.full_path)
    #  /?
    print("base_url:\n", request.base_url)
    # http://127.0.0.1:5000/
    print("root_url:\n", request.root_url)
    # http://127.0.0.1:5000/
    print("host_url:\n", request.host_url)
    # http://127.0.0.1:5000/
    return 'welcome everyone！'


if __name__ == '__main__':
    app.run()
