# 比较两个目录中的文件：filecmp.cmpfiles(dir1, dir2, common, shallow=True)
# 这个函数可以一次性比较两个目录 dir1 和 dir2 中 共同拥有 的一组文件。
# 参数说明:
#     - dir1, dir2: 要比较的两个目录的路径。
#     - common: 一个文件名列表，表示你希望比较的、在这两个目录中都存在的文件。
#     - shallow: 与 filecmp.cmp 中的含义相同。
# 返回值:
#     一个由三个列表组成的元组：(match, mismatch, errors)
#       - match: 内容相同的文件名列表。
#       - mismatch: 内容不同的文件名列表。
#       - errors: 因某些原因（如文件不存在、权限不足）无法比较的文件名列表。
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

common_files = ["a.txt", "b.txt", "d.txt"]  # d.txt 两个目录都没有

match, mismatch, errors = filecmp.cmpfiles("dir1", "dir2", common=common_files)

print(f"相同的文件: {match}")
# 输出: 相同的文件: ['a.txt']

print(f"不同的文件: {mismatch}")
# 输出: 不同的文件: ['b.txt']

print(f"无法比较的文件: {errors}")
# 输出: 无法比较的文件: ['d.txt']

# 清理
shutil.rmtree("dir1")
shutil.rmtree("dir2")
