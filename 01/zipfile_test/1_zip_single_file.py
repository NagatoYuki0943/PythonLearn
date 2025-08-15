from pathlib import Path
import zipfile


# 假设您有一个名为 "my_document.txt" 的文件
try:
    with open(Path("my_document.txt"), "w") as f:
        f.write("这是一个示例文本文件。")
except FileExistsError:
    pass


with zipfile.ZipFile(Path("single_file.zip"), "w") as zipf:
    zipf.write("my_document.txt")


# write()方法的第二个可选参数arcname可以指定文件在ZIP存档中的名称。如果不提供arcname，则默认使用原文件的路径。
with zipfile.ZipFile(Path("single_file_rename.zip"), "w") as zipf:
    zipf.write("my_document.txt", arcname="renamed_document.txt")


print("单个文件压缩成功！")
