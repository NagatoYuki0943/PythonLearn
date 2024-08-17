import time
from loguru import logger

from config import CAMERA_CONFIG


def capture():
    while True:
        with CAMERA_CONFIG["lock"]:
            EXPOSURE_TIME = CAMERA_CONFIG["EXPOSURE_TIME"]
            ANALOGUE_GAIN = CAMERA_CONFIG["ANALOGUE_GAIN"]
        logger.error(f"camera\t{EXPOSURE_TIME = }, {ANALOGUE_GAIN = }, {id(EXPOSURE_TIME) = }, {id(ANALOGUE_GAIN) = }")
        time.sleep(1)
