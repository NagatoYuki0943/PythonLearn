dummy = True
if dummy:
    # 线程
    from multiprocessing.dummy import Lock
else:
    # 进程
    from multiprocessing import Lock


class CameraConfig:
    lock = Lock() # 多线程/进程防止数据竞争
    EXPOSURE_TIME: int = 10000
    ANALOGUE_GAIN: int = 4

