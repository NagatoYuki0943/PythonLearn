# 基础使用

from datetime import datetime, timedelta
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.interval import IntervalTrigger
from apscheduler.triggers.date import DateTrigger
from apscheduler.triggers.cron import CronTrigger


# 阻塞型scheduler, 同一时刻只能有一个job运行
scheduler = BlockingScheduler()


def get_time_str():
    return f"{datetime.now():%Y-%m-%d %H:%M:%S}"


def job1_func(*args, **kwargs):
    print(f"\033[0;36;40mJob 1 executed at {get_time_str()}\033[0m")


def job2_func(*args, **kwargs):
    print(f"\033[0;32;40mJob 2 executed at {get_time_str()}\033[0m")


def job3_func(arg1, arg2, *args, **kwargs):
    print(f"\033[0;33;40mJob 3 executed at {get_time_str()}, {arg1=}, {arg2=}\033[0m")


def job4_func(*args, **kwargs):
    print(f"\033[0;31;40mJob 4 executed at {get_time_str()}\033[0m")


def job5_func(*args, **kwargs):
    print(f"\033[0;35;40mJob 5 executed at {get_time_str()}\033[0m")


# 间隔2秒执行一次
job1 = scheduler.add_job(
    job1_func,
    "interval",
    seconds=2,
    max_instances=3,  # 最多同时运行3个实例
    misfire_grace_time=60,  # 容忍60秒的任务延迟
    id="job1",
)
# 间隔4秒执行一次
job2 = scheduler.add_job(job2_func, IntervalTrigger(seconds=4), id="job2")
# 5秒后执行
job3 = scheduler.add_job(
    job3_func,
    DateTrigger(run_date=datetime.now() + timedelta(seconds=5)),
    args=["aaa"],
    kwargs={"arg2": "bbb"},
    id="job3",
)
# 当秒数为0或者5时, 执行
job4 = scheduler.add_job(job4_func, CronTrigger(second="*/5"), id="job4")
# 每个小时执行一次
job5 = scheduler.add_job(job5_func, CronTrigger(hour="*"), id="job5")


scheduler.start()
