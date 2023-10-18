"""
https://zhuanlan.zhihu.com/p/100459723

fire 可以根据任何 Python 对象自动生成命令行接口。它有如下特性：

· 能以简单的方式生成 CLI
· 是一个开发和调试 Python 代码的实用工具
· 能将现存代码或别人的代码转换为 CLI
· 使得在 Bash 和 Python 间的转换变得更容易
· 通过预先为 REPL 设置所需的模块和变量，使得实用 REPL 更加容易
"""

import fire


def train_from_folder(
    data = './data',
    new = False,
    image_size = 256,
    optimizer = 'adam',
    generate_types = ['default', 'ema'],
    log_dir = None,
):
    print("data:", data)
    print("new:", new)
    print("image_size:", image_size)
    print("optimizer:", optimizer)
    print("generate_types:", generate_types)
    print("log_dir:", log_dir)


if __name__ == "__main__":
    fire.Fire(train_from_folder)
    # > python fire_test1.py --data ./datasets --new True --optimizer lion --generate_types ema --log_dir ./logs
    # data: ./datasets
    # new: True
    # image_size: 256
    # optimizer: lion
    # generate_types: ema
    # log_dir: ./logs
