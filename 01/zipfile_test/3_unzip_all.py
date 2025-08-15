# 要将ZIP存档中的所有文件解压出来，请使用ZipFile对象的extractall()方法。
# 先运行 `1_zip_dir_use_os.py` 创建ZIP存档。
from pathlib import Path
import zipfile


# 指定解压到的目标文件夹
extract_path = Path("unzipped_all")

with zipfile.ZipFile(Path("my_folder.zip"), "r") as zipf:
    zipf.extractall(extract_path)

print(f"所有文件已解压到 '{extract_path}' 文件夹。")
