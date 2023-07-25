import sys
from termcolor import colored, cprint


"""termcolor是一个python包，可以改变控制台输出的颜色，支持各种terminal（WINDOWS的cmd.exe除外）

支持下列的文字颜色：
    grey, red, green, yellow, blue, magenta, cyan, white

支持下列的背景高亮：
    on_grey, on_red, on_green, on_yellow, on_blue, on_magenta, on_cyan, on_white

支持下列属性：
    bold, dark, underline, blink, reverse, concealed
"""

# 红色背景字符不发光
text = colored('Hello, World!', color='red')
print(text)

text = colored('Hello, World!', color='red', attrs=['reverse', 'blink'])
print(text)

# 红色背景上显示绿色字符
cprint('Hello, World!', 'green', 'on_red')

# 青蓝色背景上显示绿色字符
print_red_on_cyan = lambda x: cprint(x, color='red', on_color='on_cyan')
print_red_on_cyan('Hello, World!')
print_red_on_green = lambda x: cprint(x, color='red', on_color='on_green')
print_red_on_green('Hello, Universe!')

# 洋红色
for i in range(10):
    cprint(i, 'magenta', end=' ')

# 红色字符加粗
cprint("Attention!", 'red', attrs=['bold'], file=sys.stderr)
