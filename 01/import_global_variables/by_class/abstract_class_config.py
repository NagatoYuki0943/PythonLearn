"""使用抽象类实现全局变量的设置"""

from dataclasses import dataclass
from threading import Lock
from typing import Any


def test1():
    @dataclass
    class BaseConfig:
        lock = Lock()  # 类锁

        @classmethod
        def getattr(cls, attr_name: str) -> Any:
            with cls.lock:
                return getattr(cls, attr_name)

        @classmethod
        def setattr(cls, attr_name: str, value: Any) -> None:
            with cls.lock:
                setattr(cls, attr_name, value)

    @dataclass
    class MainConfig(BaseConfig):
        """主进程配置"""

        main_sleep_interval: int = 300  # 主循环 sleep_time ms

    @dataclass
    class CameraConfig(BaseConfig):
        exposure_time: int = 40000  # 曝光时间 微秒
        analogue_gain: float = 4.0  # 模拟增益

    # 使用继承的方式, BaseConfig 中的锁是共享的,不安全
    print(id(BaseConfig.lock))  # 2313439213952
    print(id(MainConfig.lock))  # 2313439213952
    print(id(CameraConfig.lock))  # 2313439213952


def test2():
    @dataclass
    class BaseConfig:
        @classmethod
        def getattr(cls, attr_name: str) -> Any:
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

    @dataclass
    class MainConfig(BaseConfig):
        """主进程配置"""

        lock = Lock()  # 类锁
        main_sleep_interval: int = 300  # 主循环 sleep_time ms

    @dataclass
    class CameraConfig(BaseConfig):
        lock = Lock()  # 类锁
        exposure_time: int = 40000  # 曝光时间 微秒
        analogue_gain: float = 4.0  # 模拟增益

    # 使用继承的方式, BaseConfig 中的锁是共享的,不安全
    print(id(MainConfig.lock))  # 1832438921600
    print(id(CameraConfig.lock))  # 1832438919040


if __name__ == "__main__":
    test1()
    print()
    test2()
