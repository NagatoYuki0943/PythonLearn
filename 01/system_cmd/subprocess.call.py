import subprocess


# 执行简单命令
return_code = subprocess.call(["echo", "Hello, World!"], shell=True)
print("返回码:", return_code)
# "Hello, World!"
# 返回码: 0
