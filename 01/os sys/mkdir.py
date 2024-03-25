import os

# 文件夹已存在会报错,不支持递归创建
os.mkdir('dir')

try:
    os.mkdir('dirs/a')
except:
    print('os.mkdir不支持递归创建')


# 支持递归创建
os.makedirs('dirs/a', exist_ok=True)
