import sys

# 环境变量
# print(sys.path)
[   
    'd:\\Python\\Pycharm1\\02\\day16 import\\code',     # 第一个路径是当前的路径
    'D:\\Anaconda3\\envs\\ai\\python36.zip', 
    'D:\\Anaconda3\\envs\\ai\\DLLs', 
    'D:\\Anaconda3\\envs\\ai\\lib', 
    'D:\\Anaconda3\\envs\\ai',
    'D:\\Anaconda3\\envs\\ai\\lib\\site-packages', 
    'D:\\Anaconda3\\envs\\ai\\lib\\site-packages\\win32', 
    'D:\\Anaconda3\\envs\\ai\\lib\\site-packages\\win32\\lib', 
    'D:\\Anaconda3\\envs\\ai\\lib\\site-packages\\Pythonwin'
]


# 添加自己的路径,就能使用 module 了  
sys.path.append('./module')
# sys.path.insert(0, './module')


import module

print(module.name)  # 楚留香