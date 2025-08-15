# 要压缩整个文件夹及其所有内容，最有效的方法是使用os.walk()来遍历目录树。
import os
import zipfile
from pathlib import Path


# 创建示例文件夹和文件
if not os.path.exists("my_folder"):
    os.makedirs("my_folder/sub_folder")
with open("my_folder/file_a.txt", "w") as f:
    f.write("File A")
with open("my_folder/sub_folder/file_b.txt", "w") as f:
    f.write("File B")


def zip_folder(folder_path: str | Path, output_path: str | Path):
    """
    压缩指定文件夹及其所有内容。

    :param folder_path: 要压缩的文件夹路径。
    :param output_path: 输出的ZIP文件路径。
    """
    with zipfile.ZipFile(output_path, "w", zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                # 创建ZIP内的相对路径
                relative_path = os.path.relpath(
                    os.path.join(root, file), os.path.join(folder_path, "..")
                )
                zipf.write(os.path.join(root, file), arcname=relative_path)


zip_folder("my_folder", "my_folder.zip")
print("整个文件夹压缩成功！")
