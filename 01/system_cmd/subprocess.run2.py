import subprocess


# 执行命令并捕获输出
result = subprocess.run(["python", "--version"], capture_output=True, text=True)
print("result:", result)
print("返回码:", result.returncode)
print("输出:", result.stdout)
print("错误:", result.stderr)
# result: CompletedProcess(args=['python', '--version'], returncode=0, stdout='Python 3.12.4\n', stderr='')
# 返回码: 0
# 输出: Python 3.12.4
# 错误:


result = subprocess.run(
    ["python", "-c", "import numpy as np; print(np.__version__)"],
    capture_output=True,
    text=True,
)
print("result:", result)
print("返回码:", result.returncode)
print("输出:", result.stdout)
print("错误:", result.stderr)
# result: CompletedProcess(args=['python', '-c', 'import numpy as np; print(np.__version__)'], returncode=0, stdout='1.26.4\n', stderr='')
# 返回码: 0
# 输出: 1.26.4
# 错误:
