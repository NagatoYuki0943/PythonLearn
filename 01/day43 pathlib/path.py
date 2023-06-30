import os
import pathlib


file = pathlib.Path(__file__)
print(file)                         # c:\Users\Administrator\Desktop\self\fastapi_learn\path.py
print(file.name)                    # path.py
print(file.stem)                    # path
print(file.suffix)                  # .py
print(file.parent)                  # c:\Users\Administrator\Desktop\self\fastapi_learn
print(file.is_absolute())           # True
print(file.absolute())              # c:\Users\Administrator\Desktop\self\fastapi_learn\path.py
print(file.resolve())               # C:\Users\Administrator\Desktop\self\fastapi_learn\path.py
print(file.is_dir())                # False
print(file.is_file())               # True

print(os.path.basename(__file__))   # path.py
