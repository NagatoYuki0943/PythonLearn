from colorama import init, Fore, Back, Style


#  初始化，并且设置颜色设置自动恢复
init(autoreset=True)

print(Fore.RED + 'some red text')
print(Back.GREEN + 'and with a green background')
print(Fore.BLUE + Back.CYAN + 'some red text and with a cyan background')
print(Style.DIM + 'and in dim text')
print(Style.BRIGHT + 'and in bright text')
print(Style.NORMAL + 'and in normal text')

# 如果未设置autoreset=True，需要使用如下代码重置终端颜色为初始设置
# print(Fore.RESET + Back.RESET + Style.RESET_ALL)  autoreset=True
print('back to normal now')
