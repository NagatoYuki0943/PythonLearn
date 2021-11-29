from flask import Flask, render_template

import settings

app = Flask(__name__)
app.config.from_object(settings)


# 父模板 extend
@app.route('/base')
def load_base():
    return render_template('base.html')


# 子模板 extend
@app.route('/')
def index():
    return render_template('son.html')


# 子模板 include
@app.route('/welcome')
def welcome():
    return render_template('welcome.html')


@app.route('/macro')
def use_macro():
    return render_template('macro/macro1.html')


@app.route('/macro1')
def use_macro1():
    return render_template('macro/macro2.html')


if __name__ == '__main__':
    print(app.url_map)
    app.run()
