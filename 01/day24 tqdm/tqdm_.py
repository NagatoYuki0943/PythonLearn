from tqdm import tqdm
import time

for epoch in range(100):
    pbar = tqdm(total=1000,desc=f'Epoch {epoch + 1}/100', postfix=dict, mininterval=0.1)

    for i in range(1000):
        time.sleep(0.001)
        pbar.update(1)
        # 在每一行后面添加数值
        pbar.set_postfix(**{'total_loss': 1,
                            'accuracy'  : 2,
                            'lr'        : 3})
        # Epoch 3/100:  26%|███            | 3227/12500 [00:06<00:24, 379.15it/s, accuracy=2, lr=3, total_loss=1]

