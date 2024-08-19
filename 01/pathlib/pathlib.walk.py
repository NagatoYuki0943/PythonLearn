# 类似 os.walk(), python3.12添加的

from pathlib import Path


path = Path("./")
print(path) # .


for filepath, dirnames, filenames in path.walk(top_down=True, on_error=None, follow_symlinks=False):
    print(filepath) # 遍历的路径
    print(dirnames) # 路径内的目录
    print(filenames)# 路径内的文件
    print()

# .
# ['archive', 'basename']
# ['path.py', 'pathlib.ipynb', 'pathlib.walk.py']

# archive
# []
# ['demo.txt']

# basename
# ['temp']
# ['basename.py']

# basename\temp
# []
# ['basename.py']
