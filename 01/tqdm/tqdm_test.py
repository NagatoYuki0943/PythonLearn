from tqdm import tqdm
import time
import random

for epoch in range(100):
    # 创建进度条 长度      描述                           添加其余数据的方式 显示间隔
    pbar = tqdm(total=100,desc=f'Epoch {epoch + 1}/100', postfix=dict, mininterval=0.1)

    for i in range(100):
        time.sleep(0.1)
        pbar.update(1)  # 进度条+1
        # 在每一行后面添加数值
        pbar.set_postfix(**{'total_loss': random.random(),
                            'accuracy'  : random.random(),
                            'lr'        : random.random()})
        # Epoch 2/100:  71%|█████████████     | 71/100 [00:07<00:03,  9.10it/s, accuracy=0.958, lr=0.191, total_loss=0.893]
