"""
https://click.palletsprojects.com/en/latest/
https://click-docs-zh-cn.readthedocs.io/zh/latest/

Click 是一个利用很少的代码以可组合的方式创造优雅命令行工具接口的 Python 库。 它是高度可配置的，但却有合理默认值的“命令行接口创建工具”。
"""

import click


@click.command()                                                    # 这个装饰器来装饰一个函数使它成为一个可调用的脚本
@click.option('--count', default=1, help='Number of greetings.')    # 参数
@click.option('--name', prompt='Your name',
              help='The person to greet.')
def hello(count: int, name: str):
    """Simple program that greets NAME for a total of COUNT times."""
    for x in range(count):
        click.echo(f'Hello {name}!')


if __name__ == '__main__':
    hello()

# > python click_test1.py --count=3
# <manual input your name>
# Hello Tom!
# Hello Tom!
# Hello Tom!

# > python click_test1.py --count=3 --name=Jerry
# Hello Jerry!
# Hello Jerry!
# Hello Jerry!
