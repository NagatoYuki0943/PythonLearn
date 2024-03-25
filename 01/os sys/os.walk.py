import os
# os.walk 函数将递归遍历指定文件夹


for filepath, dirnames, filenames in os.walk("./"):
    print(filepath) # 遍历的路径
    print(dirnames) # 路径内的目录
    print(filenames)# 路径内的文件
    print()

# ./
# ['basename 读取当前文件']
# ['os baisc.py', 'os.seq.py', 'os.walk.py', 'sys.path.py']

# ./basename 读取当前文件
# ['temp']
# ['basename.py']

# ./basename 读取当前文件\temp
# []
# ['basename.py'
