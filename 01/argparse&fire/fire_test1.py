# https://zhuanlan.zhihu.com/p/100459723
import fire


def train_from_folder(
    data = './data',
    new = False,
    image_size = 256,
    optimizer = 'adam',
    generate_types = ['default', 'ema'],
    log_dir = None,
):
    print("data:", data)
    print("new:", new)
    print("image_size:", image_size)
    print("optimizer:", optimizer)
    print("generate_types:", generate_types)
    print("log_dir:", log_dir)


if __name__ == "__main__":
    fire.Fire(train_from_folder)
    # > python fire_test.py --data ./datasets --new True --optimizer lion --generate_types ema --log_dir ./logs
    # data: ./datasets
    # new: True
    # image_size: 256
    # optimizer: lion
    # generate_types: ema
    # log_dir: ./logs
