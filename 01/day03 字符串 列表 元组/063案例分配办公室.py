'''

'''
import random
# 1.定义学校和办公室
school = [
    [],
    [],
    [],
]

# 2.定义老师
teachers = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
# 遍历老师列表
for teacher in teachers:
    # 3.抓阄
    # 随机数是办公室的下标
    num = random.randint(0, 2)
    # 将老师名字添加到办公室列表中
    school[num].append(teacher)


for office in school:
    print(f'该办公室老师个数为:{len(office)}')
    for teacher in office:
        print(teacher, end="\t")
    print()

# 该办公室老师个数为:2
# B	D
# 该办公室老师个数为:4
# A	F	G	H
# 该办公室老师个数为:2
# C	E
