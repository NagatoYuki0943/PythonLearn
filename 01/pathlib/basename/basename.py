import os

file_name = os.path.basename(__file__)
print(file_name)  # basename.py


with open(file_name, "r", encoding="utf-8") as f:
    txt = f.read()


with open("temp/" + file_name, "w", encoding="utf-8") as f:
    f.write(txt)
