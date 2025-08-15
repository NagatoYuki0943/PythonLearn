# 读取ZIP中文件的内容
# 先运行 `1_zip_dir_use_os.py` 创建ZIP存档。
from pathlib import Path
import zipfile


with zipfile.ZipFile(Path("my_folder.zip"), "r") as zipf:
    for name in zipf.namelist():
        print(name)
        # 读取文件内容（以字节形式）
        content = zipf.read(name)
        print(content)
        print(content.decode("utf-8"))
        print()

print("\n读取 zip 文件成功！")

# my_folder/file_a.txt
# b'File A'
# File A

# my_folder/sub_folder/file_b.txt
# b'File B'
# File B


# 读取 zip 文件成功！
