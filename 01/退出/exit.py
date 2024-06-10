# quit 和 exit 几乎一模一样, raise SystemExit Exception, 会被 try except 捕获
# quit 和 exit 来自 site module
# python 默认会自动引入 site module,但是当使用 python -S 脚本.py 时，不会引入 site module
# 所以在比较正式的代码里要使用 sys.exit() 来退出


print(0)
exit()
print(1)
