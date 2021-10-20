from tqdm import tqdm

import numpy as np

n = np.random.rand(1000)

# 会显示进度条
# 总长度
for i in tqdm(n, total=1000, desc="描述"):
    print(i)



# 以一行显示
bar = tqdm(n, total=1000, desc="描述")
for i in bar:
    bar.set_description('i:{}'.format(i))