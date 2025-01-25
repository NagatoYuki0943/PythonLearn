import os


# os.popen()
# 通过管道方式执行命令
# 返回文件对象，可以读取命令执行结果
# 支持read()和readlines()方法获取输出34


# 使用 popen 执行 ls / dir 命令并读取输出
file_stream = os.popen("dir")
print(file_stream)
# file_stream = os.popen('ls')
output = file_stream.read()
print(output)


# 使用 popen 创建新目录（虽然不常用，但可以展示如何使用）
file_stream = os.popen("mkdir new_folder_popen")
print(file_stream)
output = file_stream.read()
print(output)


# 使用 popen 获取当前日期并读取输出
date_stream = os.popen("date")
print(date_stream)
current_date = date_stream.read()
print(current_date)
