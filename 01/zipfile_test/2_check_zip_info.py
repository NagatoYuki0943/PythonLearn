# 查看ZIP文件内容
# 先运行 `1_zip_dir_use_os.py` 创建ZIP存档。
from pathlib import Path
import zipfile


with zipfile.ZipFile(Path("my_folder.zip"), "r") as zipf:
    print("printdir:")
    zipf.printdir()

    print("\nnamelist:")
    for name in zipf.namelist():
        print(name)

    print("\nfilelist:")
    for file in zipf.filelist:
        print(
            f"filename: {file.filename}, compress_type: {file.compress_type}, compress_size: {file.compress_size}, file_size: {file.file_size}, date_time: {file.date_time}"
        )

    # same as above
    print("\ninfolist:")
    for file in zipf.infolist():
        print(
            f"filename: {file.filename}, compress_type: {file.compress_type}, compress_size: {file.compress_size}, file_size: {file.file_size}, date_time: {file.date_time}"
        )


print("\n查看 zip 文件成功！")

# printdir:
# File Name                                             Modified             Size
# my_folder/file_a.txt                           2025-08-15 09:24:48            6
# my_folder/sub_folder/file_b.txt                2025-08-15 09:24:48            6

# namelist:
# my_folder/file_a.txt
# my_folder/sub_folder/file_b.txt

# filelist:
# filename: my_folder/file_a.txt, compress_type: 8, compress_size: 8, file_size: 6, date_time: (2025, 8, 15, 9, 24, 48)
# filename: my_folder/sub_folder/file_b.txt, compress_type: 8, compress_size: 8, file_size: 6, date_time: (2025, 8, 15, 9, 24, 48)

# infolist:
# filename: my_folder/file_a.txt, compress_type: 8, compress_size: 8, file_size: 6, date_time: (2025, 8, 15, 9, 24, 48)
# filename: my_folder/sub_folder/file_b.txt, compress_type: 8, compress_size: 8, file_size: 6, date_time: (2025, 8, 15, 9, 24, 48)

# 查看 zip 文件成功！
