# 深度比较目录：filecmp.dircmp(a, b, ignore=None, hide=None)
# 这是 filecmp 模块中最强大和复杂的功能。它会创建一个目录比较对象 (dircmp 对象)，让你能够递归地、详细地分析两个目录 a 和 b 之间的差异。
# 参数说明:
#     - a, b: 要比较的两个目录的路径。
#     - ignore: 一个需要忽略的文件名或目录名列表（例如 ['.DS_Store', '__pycache__']）。
#     - hide: 一个在报告中隐藏的文件名或目录名列表（默认是 [os.curdir, os.pardir]，即 . 和 ..）。
# dircmp 对象的重要属性:
#     - left_only: 仅存在于左侧目录（a）中的文件和目录列表。
#     - right_only: 仅存在于右侧目录（b）中的文件和目录列表。
#     - common: 在两个目录中都存在的文件和目录列表。
#     - common_files: 在两个目录中都存在的文件列表。
#     - common_dirs: 在两个目录中都存在的目录列表。
#     - same_files: 内容相同的共同文件列表。
#     - diff_files: 内容不同的共同文件列表。
#     - funny_files: 因某些原因（例如类型不同，一个是文件一个是目录）无法比较的共同文件列表。
# dircmp 对象的重要方法:
#     - report(): 打印一个简洁的比较报告。
#     - report_partial_closure(): 打印从当前目录到所有子目录的比较报告。
#     - report_full_closure(): 递归地打印所有共同子目录的完整比较报告。

import filecmp
import os
import shutil

# 创建目录和文件结构
os.makedirs("dir1", exist_ok=True)
os.makedirs("dir2", exist_ok=True)

with open("dir1/a.txt", "w") as f:
    f.write("file a")
with open("dir1/b.txt", "w") as f:
    f.write("file b")
with open("dir1/c.txt", "w") as f:
    f.write("file c")  # dir2 中没有 c.txt

with open("dir2/a.txt", "w") as f:
    f.write("file a")  # a.txt 内容相同
with open("dir2/b.txt", "w") as f:
    f.write("file B")  # b.txt 内容不同

dc = filecmp.dircmp("dir1", "dir2")

print("--- 简洁报告 ---")
dc.report()
# 输出:
# --- 简洁报告 ---
# cmp dir1 dir2
# Only in dir1 : ['c.txt']
# Identical files : ['a.txt']
# Differing files : ['b.txt']

print("\n--- 详细属性访问 ---")
print(f"仅在 dir1 中的: {dc.left_only}")
# 输出: 仅在 dir1 中的: ['c.txt']

print(f"内容相同的文件: {dc.same_files}")
# 输出: 内容相同的文件: ['a.txt']

print(f"内容不同的文件: {dc.diff_files}")
# 输出: 内容不同的文件: ['b.txt']


# 清理
shutil.rmtree("dir1")
shutil.rmtree("dir2")
