import os
from pathlib import Path

path = Path(__file__)

print(path)  # d:\ml\code\test\path\path.py
print(path.name)  # path.py
print(path.stem)  # path
print(path.suffix)  # .py
print(path.suffixes)  # ['.py']

print(path.anchor)  # d:\
print(path.drive)  # d:

print(path.parts)  # ('d:\\', 'ml', 'code', 'test', 'path', 'path.py')
print(path.parent)  # d:\ml\code\test\path
print()
for p in path.parents:
    print(p)
print()
# d:\ml\code\test\path
# d:\ml\code\test
# d:\ml\code
# d:\ml
# d:\

print(path.is_absolute())  # True
print(path.absolute())  # d:\ml\code\test\path\path.py
print(path.resolve())  # D:\ml\code\test\path\path.py
print(path.is_file())  # True
print(path.is_dir())  # False
print(path.exists())  # True

print(path.root)  # \

print(os.path.basename(__file__))  # path.py
