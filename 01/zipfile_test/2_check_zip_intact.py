# 检查ZIP文件完整性
# 先运行 `1_zip_dir_use_os.py` 创建ZIP存档。
from pathlib import Path
import zipfile

try:
    with zipfile.ZipFile(Path("my_folder.zip"), "r") as zipf:
        # 测试ZIP文件完整性
        bad_file = zipf.testzip()
        if bad_file:
            print(f"损坏的文件: {bad_file}")
        else:
            print("ZIP文件完整")
except zipfile.BadZipFile:
    print("文件不是有效的ZIP文件")
