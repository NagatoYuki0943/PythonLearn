dummy = True
if dummy:
    # 线程
    from multiprocessing.dummy import Lock
else:
    # 进程
    from multiprocessing import Lock
from dataclasses import dataclass
from typing import Any
from loguru import logger


@dataclass
class BaseConfig:
    @classmethod
    def getattr(cls, attr_name: str) -> Any:
        assert hasattr(cls, attr_name), f"{attr_name} not in {cls.__name__}"
        if hasattr(cls, "lock"):
            with cls.lock:
                return getattr(cls, attr_name)
        else:
            return getattr(cls, attr_name)

    @classmethod
    def setattr(cls, attr_name: str, value: Any) -> None:
        if hasattr(cls, "lock"):
            with cls.lock:
                setattr(cls, attr_name, value)
        else:
            setattr(cls, attr_name, value)


class CameraConfig(BaseConfig):
    # lock = Lock() # 多线程/进程防止数据竞争
    exposure_time: int = 10000
    analogue_gain: int = 4
