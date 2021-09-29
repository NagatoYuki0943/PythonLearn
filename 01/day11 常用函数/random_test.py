import random


# 1.random.random() 0到1的随机浮点数
a = random.random()
print(a)                                # 0.41690357829630875
print('*' * 50)


# 2.random.uniform(a,b)  指定范围浮点数
print(random.uniform(1,10))             # 6.8122370433101676
print(random.uniform(10,1))             # 7.643295020974139
print('*' * 50)


# 3.random.randint(a, b) 指定范围整数
print(random.randint(1,10))             # 7
print('*' * 50)


# 4.random.randrange([start], stop[, step]) 范围选取一个
# random.randrange(10, 30, 2)，结果相当于从[10, 12, 14, 16, ... 26, 28]序列中获取一个随机数。
# random.randrange(10, 30, 2)在结果上与 random.choice(range(10, 30, 2) 等效。
print(random.randrange(10, 30, 2))      # 12
print(random.choice(range(10, 30, 2)))  # 22
print('*' * 50)


# 5.random.choice(sequence) 选择
lst = ['python','C','C++','javascript']  
str1 = ('I love python')  
print(random.choice(lst))               # javascript
print(random.choice(str1))              # o
print('*' * 50)


# 6.random.shuffle(x[, random]) 打乱 不需要返回值,直接修改原列表
p = ['A' , 'B', 'C', 'D', 'E' ]
random.shuffle(p)  
print (p)                               # ['D', 'E', 'C', 'A', 'B']
print('*' * 50)


# 7.random.sample(sequence, k) 取样
lst = [1, 2, 3, 4, 5]  
print(random.sample(lst, 4))             # [2, 3, 4, 1]
print(lst)                              # [1, 2, 3, 4, 5]


