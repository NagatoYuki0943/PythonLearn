# 原理和 exit, quit 一样, raise SystemExit Exception, 会被 try except 捕获
# quit 和 exit 来自 site module
# python 默认会自动引入 site module,但是当使用 python -S 脚本.py 时，不会引入 site module
# 所以在比较正式的代码里要使用 sys.exit() 来退出


import sys


print(0)
sys.exit()
print(1)
