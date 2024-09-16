"""
产生随机数
"""

import random

# 返回一个随机整数 [a, b]
print(random.randint(1, 10))  # 3


# 随机小数,[a ~ b)
print(random.random())  # 0.7397832283752886


# 获取范围中的随机数 [a, b]
print(random.uniform(1.43, 2.5))  # 2.0227622260858937


# 从列表随机选择一个
names = ["itcast", "itheima", "baoxuegu"]
print(random.choice(names))
