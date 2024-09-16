import time
from threading import Thread
from loguru import logger

from camera import capture
from config import CameraConfig


def main():
    t = Thread(target=capture, daemon=True)
    t.start()

    i = 0
    while True:
        if i >= 5 and i < 10:
            CameraConfig.setattr(attr_name="exposure_time", value=20000)
            CameraConfig.setattr(attr_name="analogue_gain", value=3)
        elif i >= 10 and i < 15:
            CameraConfig.setattr(attr_name="exposure_time", value=30000)
            CameraConfig.setattr(attr_name="analogue_gain", value=2)
        elif i >= 15 and i < 20:
            CameraConfig.setattr(attr_name="exposure_time", value=40000)
            CameraConfig.setattr(attr_name="analogue_gain", value=1)
        elif i >= 20:
            break

        exposure_time = CameraConfig.getattr("exposure_time")
        analogue_gain = CameraConfig.getattr("analogue_gain")
        logger.success(
            f"main\t{exposure_time = }, {analogue_gain = }, {id(exposure_time) = }, {id(analogue_gain) = }"
        )

        time.sleep(1)
        i += 1


if __name__ == "__main__":
    main()
