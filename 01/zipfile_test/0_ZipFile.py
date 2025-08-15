# zipfile模块的核心是ZipFile类。您可以通过实例化这个类来处理ZIP文件。
# 最常见的用法是通过with语句，这样可以确保在操作完成后自动关闭ZIP文件，即使发生错误也能正确处理。

import zipfile

# 创建或打开一个ZIP文件
with zipfile.ZipFile("archive.zip", "w") as zipf:
    # 在这里执行压缩操作
    pass

# 读取一个ZIP文件
with zipfile.ZipFile("archive.zip", "r") as zipf:
    # 在这里执行解压操作
    pass

# 模式（Mode）参数：
# - "r"：读取一个已存在的ZIP文件（默认模式）。
# - "w"：创建一个新的ZIP文件。如果文件已存在，则会覆盖它。
# - "a"：向一个已存在的ZIP文件追加内容。如果文件不存在，则会创建一个新的。
# - "x"：独占创建模式，仅当文件不存在时创建。如果文件已存在，会抛出FileExistsError。
