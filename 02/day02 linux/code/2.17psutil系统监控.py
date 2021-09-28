'''
psutil 可以获取 cpu,ram,disk,net,time
'''
import datetime
import psutil


# 1.获取cpu的核心数
cpu_logic_nums = psutil.cpu_count()
print(cpu_logic_nums)                           # 6
# 获取物理核心数
cpu_nums = psutil.cpu_count(logical=False)
print(cpu_nums)                                 # 6


# 2.获取cpu使用率  interval=0.5 获取间隔
cpu_usage = psutil.cpu_percent(interval=0.5)    # 22.1
print(cpu_usage)
# 获取每一核CPU的使用率
per_cpu_usage = psutil.cpu_percent(interval=0.5, percpu=True)
print(per_cpu_usage)                            # [6.1, 6.2, 18.8, 25.0, 21.9, 6.2]


# 3.获取内存信息
memory_usage = psutil.virtual_memory()
print(memory_usage)     #svmem(total=17123737600, available=4217442304, percent=75.4, used=12906295296, free=4217442304)
# 获取使用率可用,已使用
print(memory_usage.percent)                     # 74.8
print(memory_usage.available/1024/1024/1024)    # 4.004596710205078
print(memory_usage.used/1024/1024/1024)         # 11.943126678466797


# 4.获取硬盘使用率
disk_part = psutil.disk_partitions()
print(disk_part)                                # [sdiskpart(device='C:\\', mountpoint='C:\\', ...
# 获取指定路径
disk_usage = psutil.disk_usage('/')
print(disk_usage)                               # sdiskusage(total=1000186310656, used=517084291072, free=483102019584, percent=51.7)


# 5.获取网络信息
net_info = psutil.net_io_counters()
print(net_info)
net_recv = psutil.net_io_counters().bytes_recv
print(net_recv/1024/1024)
net_sent = psutil.net_io_counters().bytes_sent
print(net_sent/1024/1024)


# 6.获取开机时间  unix时间
start_time = datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")
print(start_time)   # 2021-05-31 09:00:24

