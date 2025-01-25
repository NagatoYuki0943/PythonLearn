import subprocess


# 使用管道获取命令输出
process = subprocess.Popen(
    ["echo", "Hello, World!"], shell=True, stdout=subprocess.PIPE, text=True
)
output, error = process.communicate()
print("output: ", output)
print("error: ", error)
# output:  "Hello, World!"
# error:  None


# 执行多个命令
# 使用 ls / dir 命令并通过 grep / findstr 过滤结果
ls_process = subprocess.Popen(["dir"], shell=True, stdout=subprocess.PIPE, text=True)
grep_process = subprocess.Popen(
    ["findstr", "os"],
    stdin=ls_process.stdout,
    shell=True,
    stdout=subprocess.PIPE,
    text=True,
)
output, error = grep_process.communicate()
print("output: \n", output)
print("error: ", error)
# output:
# 2025/01/25 周六  10:19               716 os.popen.py
# 2025/01/25 周六  10:28               570 os.system.py
# error:  None
