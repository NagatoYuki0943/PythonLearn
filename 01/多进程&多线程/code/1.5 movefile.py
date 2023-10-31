from tqdm import tqdm
from multiprocessing import Process
from shutil import move, copy
from pathlib import Path
import random


strs = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

def generate(path: Path, numbers: int = 5):
    path = Path(path)
    path.mkdir(parents=True, exist_ok=True)
    for _ in range(numbers):
        name = "".join(random.sample(strs, 4)) + ".txt"
        content = "".join(random.sample(strs, 20))
        with open(path / name, mode="w", encoding="utf-8") as f:
            f.write(content)


def mv(src: Path, dst: Path):
    src = Path(src)
    assert src.exists(), f"{str(src)} is not exists"
    dst = Path(dst)
    dst.mkdir(parents=True, exist_ok=True)
    for file in tqdm(src.glob('*.txt')):
        new_file = dst / file.name
        # move(file, new_file)
        copy(file, new_file)


if __name__ == "__main__":
    generate("./src")
    # mv("./src", "./dst")
    # move不能这样使用,因为2个线程同时移动相同的数据会导致文件找不到
    # copy可以使用,不过没意义,因为相当于复制了2遍
    # 正确的方式是不同进程传入不同的数据路径,分别移动/复制,可以加快速度
    processes: list[Process] = []

    for i in range(2):
        processes.append(Process(target=mv, args=("./src", "./dst")))

    for p in processes:
        p.start()

    for p in processes:
        p.join()

    for p in processes:
        p.close()
