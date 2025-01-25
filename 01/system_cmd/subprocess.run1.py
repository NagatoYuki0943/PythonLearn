import subprocess


# 执行简单的 echo 命令
result = subprocess.run(
    ["echo", "Hello World"], shell=True, capture_output=True, text=True
)
print("result:", result)
print("返回码:", result.returncode)
print("输出:", result.stdout)
print("错误:", result.stderr)
# result: CompletedProcess(args=['echo', 'Hello World'], returncode=0, stdout='"Hello World"\n', stderr='')
# 返回码: 0
# 输出: "Hello World"
# 错误:


# 列出当前目录文件
result = subprocess.run(["dir"], shell=True, capture_output=True, text=True)
print("result:", result)
print("返回码:", result.returncode)
print("输出:", result.stdout)
print("错误:", result.stderr)
# result: CompletedProcess(args=['dir'], returncode=0, stdout=' 驱动器 D 中的卷没有标签。\n 卷的序列号是 62F1-39AB\n\n D:\\Python\\PythonLearn\\01\\system_cmd 的目录\n\n2025/01/25 周
# 六  10:19    <DIR>          .\n2025/01/25 周六  10:19    <DIR>          ..\n2025/01/25 周六  10:19    <DIR>          .ruff_cache\n2025/01/25 周六  09:42    <DIR>          new_folder_popen\n2025/01/25 周六  10:19               716 os.popen.py\n2025/01/25 周六  10:19               568 os.system.py\n2025/01/25 周六  10:27               522 subprocess.run1.py\n2025/01/25 周六  10:26               902 subprocess.run2.py\n               4 个文件          2,708 字节\n               4 个目录 273,542,053,888 可用字节\n', stderr='')
# 返回码: 0
# 输出:  驱动器 D 中的卷没有标签。
#  卷的序列号是 62F1-39AB

#  D:\Python\PythonLearn\01\system_cmd 的目录

# 2025/01/25 周六  10:19    <DIR>          .
# 2025/01/25 周六  10:19    <DIR>          ..
# 2025/01/25 周六  10:19    <DIR>          .ruff_cache
# 2025/01/25 周六  09:42    <DIR>          new_folder_popen
# 2025/01/25 周六  10:19               716 os.popen.py
# 2025/01/25 周六  10:19               568 os.system.py
# 2025/01/25 周六  10:27               522 subprocess.run1.py
# 2025/01/25 周六  10:26               902 subprocess.run2.py
#                4 个文件          2,708 字节
#                4 个目录 273,542,053,888 可用字节
# 错误:
