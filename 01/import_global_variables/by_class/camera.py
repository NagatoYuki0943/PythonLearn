import time
from loguru import logger

from config import CameraConfig


def capture():
    while True:
        exposure_time = CameraConfig.getattr("exposure_time")
        analogue_gain = CameraConfig.getattr("analogue_gain")
        logger.error(
            f"camera\t{exposure_time = }, {analogue_gain = }, {id(exposure_time) = }, {id(analogue_gain) = }"
        )
        time.sleep(1)
