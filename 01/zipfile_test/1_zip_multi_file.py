from pathlib import Path
import zipfile


# 创建一些示例文件
file_list = ["multiple_file1.txt", "multiple_file2.txt", "multiple_image.jpg"]
for filename in file_list:
    with open(Path(filename), "w") as f:
        f.write(f"这是 {filename} 的内容。")


with zipfile.ZipFile(Path("multiple_files.zip"), "w") as zipf:
    for file in file_list:
        zipf.write(file)


print("多个文件压缩成功！")
