dummy = True
if dummy:
    # 线程
    from multiprocessing.dummy import Lock
else:
    # 进程
    from multiprocessing import Lock


# 需要把不可变类型放入可变类型中，才能实现在一个文件中修改变量，在另一个文件中使用修改的变量
CAMERA_CONFIG = {
    "lock": Lock(),
    "EXPOSURE_TIME": 10000,   # 曝光时间
    "ANALOGUE_GAIN": 4,       # 模拟增益
}
