# zipfile.extract() 方法的设计初衷就是为了忠实地还原压缩时的文件结构，所以它默认会保留完整的路径。要在解压单个文件时忽略其在压缩包内的目录结构，您不能直接使用 extract()，而是需要采取“读取-写入”的策略。
# 思路很简单：
# 从 ZIP 存档中读取目标文件的二进制内容到内存中。
# 在您指定的本地路径下，创建一个新文件并写入这些内容。
# 先运行 `1_zip_dir_use_os.py` 创建ZIP存档。

import zipfile
from pathlib import Path


# 定义解压后的目标文件夹和新文件名
output_dir = Path("unzipped_flat")
output_dir.mkdir(exist_ok=True)  # 创建目标文件夹


with zipfile.ZipFile("my_folder.zip", "r") as zipf:
    namelist = zipf.namelist()
    for name in namelist:
        output_path = output_dir / name.split("/")[-1]  # 直接保存为文件名

        # 1. 从ZIP文件中读取文件的二进制内容
        file_content = zipf.read(name)

        # 2. 将内容写入到本地的新文件中
        output_path.write_bytes(file_content)

        print(f"\n成功将 '{name}' 解压为 '{output_path}'，已忽略原始路径。")
