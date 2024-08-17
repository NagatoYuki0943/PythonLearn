import time
from loguru import logger

from config import CameraConfig


def capture():
    while True:
        with CameraConfig.lock:
            EXPOSURE_TIME = CameraConfig.EXPOSURE_TIME
            ANALOGUE_GAIN = CameraConfig.ANALOGUE_GAIN
        logger.error(f"camera\t{EXPOSURE_TIME = }, {ANALOGUE_GAIN = }, {id(EXPOSURE_TIME) = }, {id(ANALOGUE_GAIN) = }")
        time.sleep(1)
