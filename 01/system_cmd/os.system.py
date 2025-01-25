import os


# os.system()
# 最简单直接的方法
# 在子终端运行系统命令
# 只返回命令执行状态（0表示成功，非0表示失败）
# 无法获取命令输出结果14


# 执行 dir / ls 命令以列出当前目录的文件
ok = os.system("dir")
# ok = os.system("ls")
print(ok)  # 0 表示成功，非0表示失败


# 创建新目录
# 创建一个名为 new_folder 的新目录
ok = os.system("mkdir new_folder")
print(ok)  # 0


# 获取当前日期
# 获取并打印当前日期
ok = os.system("date")
print(ok)  # 0
