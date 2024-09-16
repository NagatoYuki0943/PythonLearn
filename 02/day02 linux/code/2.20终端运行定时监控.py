# 1.导入包
import datetime
import psutil


def monitor(time):
    # 2.定义变量保存CPU的使用率
    cpu_per = psutil.cpu_percent(interval=time)

    # 3、定义变量保存内存信息
    memory_info = psutil.virtual_memory()

    # 4、定义变量保存硬盘的信息
    disk_info = psutil.disk_usage("/")  # 指定目录

    # 5、定义变量保存网络的信息
    net_info = psutil.net_io_counters()

    # 获取系统当前时间                  now返回的是秒
    current_time = datetime.datetime.now().strftime("%F %T")

    # 6、拼接字符串显示   % 占位  %(值1,值2)
    log_str = "|-------------------|------------|-------------|-------------|-----------------------------|\n"
    log_str += "|      监控时间       |  CPU使用率  |   内存使用率  |   硬盘使用率  |          网络收发量           |\n"
    log_str += (
        "|                   | (共%d核CPU)  |  (总计%dG内存) | (总计%dG硬盘)|                           |\n"
        % (
            psutil.cpu_count(logical=False),
            memory_info.total / 1024 / 1024 / 1024,
            disk_info.total / 1024 / 1024 / 1024,
        )
    )
    log_str += "|-------------------|------------|-------------|-------------|----------------------------|\n"
    log_str += "|%s|    %s%%   |    %s%%    |    %s%%    |   收:%s/发:%s  |\n" % (
        current_time,
        cpu_per,
        memory_info.percent,
        disk_info.percent,
        net_info.bytes_recv,
        net_info.bytes_sent,
    )
    log_str += "|-------------------|------------|-------------|-------------|----------------------------|\n"
    print(log_str)

    # 7、保存监控信息到日志文件 a 追加文件
    f = open("2.20.log", "a", encoding="utf-8")
    f.write(log_str + "\n\n")
    f.close()


# 无限执行
if __name__ == "__main__":
    # 死循环
    while True:
        monitor(3)
