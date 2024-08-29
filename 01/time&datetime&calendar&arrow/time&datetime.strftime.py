import time
from datetime import datetime


# 获取当前时间戳
current_time = time.localtime()
# 使用 strftime 格式化到秒级别
formatted_time = time.strftime("%Y%m%d-%H%M%S", current_time)
print(formatted_time)
# 20240829-112616

# 获取当前时间
now = datetime.now()
# 格式化时间戳，包含毫秒
formatted_time_with_milliseconds = now.strftime("%Y%m%d-%H%M%S.%f")
print(formatted_time_with_milliseconds)
# 20240829-112616.982207
