'''
读文件:
    c = csv.reader(open(???))
    for i in c:
        print(i)

写文件:
    c = csv.writer(open(???, newline=''))
    c.writerow()
    c.writerows()
'''
import csv


# 1.读文件
with open('1.csv', mode='r', encoding='utf-8') as f:
    c = csv.reader(f)
    for i in c:
        print(i)
        # ['测试1', '软件测试工程师']
        # ['测试2', '软件测试工程师']
        # ['测试3', '软件测试工程师']
        # ['测试4', '软件测试工程师']
        # ['测试5', '软件测试工程师']





data = [
    ["测试1",'软件测试工程师'],
    ["测试2",'软件测试工程师'],
    ["测试3",'软件测试工程师'],
    ["测试4",'软件测试工程师'],
    ["测试5",'软件测试工程师'],
]

# newline='' 是因为csv写入有空行,用了这个参数就没有了
with open('2.csv', mode='w', encoding='utf-8', newline='') as f:
    c = csv.writer(f,)

    c.writerows([[1, 2],[4, 5]])
    for i in data:
        c.writerow(i)