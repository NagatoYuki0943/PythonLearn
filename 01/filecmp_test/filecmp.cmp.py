# 比较单个文件：filecmp.cmp(f1, f2, shallow=True)
# 这是最基础的比较功能，用于判断两个文件 f1 和 f2 是否完全相同。
# 参数说明:
#     - f1, f2: 要比较的两个文件的路径（字符串）。
#     - shallow (浅比较):
#         - True (默认值): 这是“浅”比较。它首先会比较两个文件的 os.stat() 信息（如文件大小、修改时间等）。如果这些元数据不同，就认为文件不同，不再继续比较内容。如果元数据相同，才会去逐字节比较文件内容。这种方式速度更快。
#         - False: 这是“深”比较。它不关心文件的元数据，直接逐字节比较两个文件的内容。
# 返回值:
#     如果文件相同，返回 True。
#     如果文件不同，返回 False。

import filecmp
import os

# 创建两个相同的文件
with open("file1.txt", "w") as f:
    f.write("Hello Python")
with open("file2.txt", "w") as f:
    f.write("Hello Python")

# 创建一个不同的文件
with open("file3.txt", "w") as f:
    f.write("Hello World")

# 浅比较 (默认)
print(f"file1 和 file2 是否相同? {filecmp.cmp('file1.txt', 'file2.txt')}")
# 输出: file1 和 file2 是否相同? True

# 深比较
print(
    f"file1 和 file3 是否相同 (深比较)? {filecmp.cmp('file1.txt', 'file3.txt', shallow=False)}"
)
# 输出: file1 和 file3 是否相同 (深比较)? False

# 清理文件
os.remove("file1.txt")
os.remove("file2.txt")
os.remove("file3.txt")
