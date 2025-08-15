# 解压ZIP存档中的特定文件，可以使用extract()方法。
# 首先，您可能需要知道存档中有哪些文件。可以使用namelist()或printdir()方法查看。
# 先运行 `1_zip_dir_use_os.py` 创建ZIP存档。
from pathlib import Path
import zipfile


with zipfile.ZipFile(Path("my_folder.zip"), "r") as zipf:
    namelist = zipf.namelist()
    for name in namelist:
        # 解压单个文件
        # 会自动创建unzipped_single文件夹, 并解压到该文件夹下,目录和压缩文件中保持一致
        zipf.extract(name, path="unzipped_single/")

print("\n指定文件解压成功！")
