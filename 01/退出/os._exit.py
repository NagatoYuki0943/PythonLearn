# os._exit() 调用 systemcall 函数
# 强制退出,不管其他情况
# 不会被 try except 捕获


import os

try:
    print(0)
    os._exit(1) # status=0代表正常,其余代表异常
    print(1)
except SystemExit:
    print(2)

print(3)
# 0


