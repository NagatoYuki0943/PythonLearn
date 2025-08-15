from pathlib import Path
import zipfile


# 假设您有一个名为 "my_document.txt" 的文件
try:
    with open(Path("my_document.txt"), "w") as f:
        f.write("这是一个示例文本文件。")
except FileExistsError:
    pass

# 不同的压缩级别
with zipfile.ZipFile(
    "zip_level.zip", "w", zipfile.ZIP_DEFLATED, compresslevel=9
) as zipf:
    zipf.write("my_document.txt")  # 最高压缩级别


# 可用的压缩方法
# zipfile.ZIP_STORED     # 不压缩
# zipfile.ZIP_DEFLATED   # 标准压缩（推荐）
# zipfile.ZIP_BZIP2      # BZIP2压缩
# zipfile.ZIP_LZMA       # LZMA压缩

print("单个文件压缩成功！")
