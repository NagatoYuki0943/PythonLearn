"""
while 判断条件1:
    代码1
    while 判断条件2:
        代码2
"""

i = 1
while i <= 9:
    j = 1
    while j <= i:
        print(f"{j}*{i}={i * j}", end="\t")
        j += 1
    i += 1
    print()
