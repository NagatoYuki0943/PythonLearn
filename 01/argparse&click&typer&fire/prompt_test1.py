# https://www.jianshu.com/p/996951e5e9f3
"""
prompt_toolkit 用于打造交互式命令行，在交互式场景的使用中

prompt_toolkit 具有以下特点：
    - 语法高亮
    - 支持多行编辑
    - 支持代码补全
    - 支持自动提示
    - 使用鼠标移动光标
    - 支持查询历史
    - 对 Unicode 支持良好
    - 跨平台
    - 支持 Emacs 与 Vi 风格的快捷键
"""

from prompt_toolkit import prompt
from prompt_toolkit.history import FileHistory
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from prompt_toolkit.contrib.completers import SystemCompleter


while True:
    user_input = prompt(
        message=">>>",
        history=FileHistory("history.txt"),  # 历史记录
        auto_suggest=AutoSuggestFromHistory(),  # 根据历史记录自动建议
        completer=SystemCompleter(),  # 系统命令自动补全
    )
    if user_input.strip().lower() == "exit":
        break
    print(user_input)
