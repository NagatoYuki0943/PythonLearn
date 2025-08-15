# 要压缩整个文件夹及其所有内容，最有效的方法是使用os.walk()来遍历目录树。

import zipfile
from pathlib import Path

# --- 1. 使用 Pathlib 创建示例文件和文件夹 ---

# 创建一个 Path 对象代表主文件夹
folder = Path("my_folder_pathlib")
# 使用 '/' 操作符构建子文件夹路径
sub_folder = folder / "sub_folder"

# exist_ok=True 行为类似于 os.makedirs，如果文件夹已存在则不报错
# parents=True 行为类似于 os.makedirs，会自动创建任何不存在的父目录
sub_folder.mkdir(parents=True, exist_ok=True)

# 使用 Path 对象的 write_text() 方法轻松创建文件和写入内容
(folder / "file_a.txt").write_text("File A from pathlib")
(sub_folder / "file_b.txt").write_text("File B from pathlib")


def zip_folder_pathlib(folder_path: str | Path, output_path: str | Path):
    """使用 pathlib 压缩指定文件夹及其所有内容。

    Args:
        folder_path (str | Path): 待压缩文件夹的路径
        output_path (str | Path): 压缩包输出路径
    """
    # 将输入路径统一转换为 Path 对象，增加函数的灵活性
    folder_to_zip = Path(folder_path)
    output_zip_path = Path(output_path)

    with zipfile.ZipFile(output_zip_path, "w", zipfile.ZIP_DEFLATED) as zipf:
        # Path.rglob('*') 是一个强大的生成器，可以递归地查找所有文件和目录
        # 它等同于 os.walk 的功能
        # Path().walk() 也可以实现 os.walk 的功能
        for file in folder_to_zip.rglob("*"):
            # 确保我们只添加文件，不添加文件夹
            if file.is_file():
                # file.relative_to() 是 os.path.relpath 的面向对象替代方法
                # 我们计算文件相对于 "待压缩文件夹的父目录" 的路径
                # 这可以确保压缩包内包含顶级文件夹本身 (即 'my_folder_pathlib')
                # 这与原代码的行为完全一致
                arcname = file.relative_to(folder_to_zip.parent)
                zipf.write(file, arcname=arcname)


# 调用新函数
zip_folder_pathlib("my_folder_pathlib", "folder_pathlib.zip")
print("使用 pathlib 整个文件夹压缩成功！")
