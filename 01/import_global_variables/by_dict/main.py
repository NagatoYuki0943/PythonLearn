import time
from threading import Thread
from loguru import logger

from camera import capture
from config import CAMERA_CONFIG


def main():
    t = Thread(target=capture, daemon=True)
    t.start()

    i = 0
    while True:
        if i >= 5 and i < 10:
            with CAMERA_CONFIG["lock"]:
                CAMERA_CONFIG["EXPOSURE_TIME"] = 20000
                CAMERA_CONFIG["ANALOGUE_GAIN"] = 3
        elif i >= 10 and i < 15:
            with CAMERA_CONFIG["lock"]:
                CAMERA_CONFIG["EXPOSURE_TIME"] = 30000
                CAMERA_CONFIG["ANALOGUE_GAIN"] = 2
        elif i >= 15 and i < 20:
            with CAMERA_CONFIG["lock"]:
                CAMERA_CONFIG["EXPOSURE_TIME"] = 40000
                CAMERA_CONFIG["ANALOGUE_GAIN"] = 1
        elif i >= 20:
            break

        with CAMERA_CONFIG["lock"]:
            EXPOSURE_TIME = CAMERA_CONFIG["EXPOSURE_TIME"]
            ANALOGUE_GAIN = CAMERA_CONFIG["ANALOGUE_GAIN"]
        logger.success(
            f"main\t{EXPOSURE_TIME = }, {ANALOGUE_GAIN = }, {id(EXPOSURE_TIME) = }, {id(ANALOGUE_GAIN) = }"
        )

        time.sleep(1)
        i += 1


if __name__ == "__main__":
    main()
