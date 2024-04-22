import os

# 获取环境变量
ak = os.getenv("OPENXLAB_AK", "")
sk = os.getenv("OPENXLAB_SK", "")
print(ak)
print(sk)
