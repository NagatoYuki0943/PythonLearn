import typer
from typing_extensions import Annotated

# 创建一个 Typer 应用实例
app = typer.Typer()

@app.command()
def hello(
    name: str,
    count: Annotated[int, typer.Option("--count", "-c", help="问候的次数。")] = 1,
    shout: Annotated[bool, typer.Option("--shout", help="使用大写字母输出。")] = False,
):
    """
    一个使用 typer 的简单问候程序。
    """
    message = f"你好, {name}!"
    if shout:
        message = message.upper()

    for _ in range(count):
        print(message)

if __name__ == "__main__":
    app()

# 查看帮助信息
# python typer_test.py --help

# 基本用法
# python typer_test.py Alice
# 你好, Alice!


# 使用可选参数
# python typer_test.py Bob --count 3
# 你好, Bob!
# 你好, Bob!
# 你好, Bob!

# 使用布尔标志
# python typer_test.py Cindy --shout
# 你好, CINDY!

# 组合使用
# python typer_test.py David -c 2 --shout
# 你好, DAVID!
# 你好, DAVID!
