# raise SystemExit Exception, 会被 try except 捕获
# 在这里没有退出程序


import sys


try:
    print(0)
    exit()
    print(1)
except SystemExit:
    print(2)

print(3)
# 0
# 2
# 3


try:
    print(0)
    quit()()
    print(1)
except SystemExit:
    print(2)

print(3)
# 0
# 2
# 3


try:
    print(0)
    sys.exit()
    print(1)
except SystemExit:
    print(2)

print(3)
# 0
# 2
# 3


try:
    print(0)
    raise SystemExit # 自己 raise SystemExit 效果是一样的
    print(1)
except SystemExit:
    print(2)

print(3)
# 0
# 2
# 3