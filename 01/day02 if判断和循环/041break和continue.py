'''
1. break 和 continue 是 python 两个关键字
2. break 和 continue 只能用在循环中
3. break 是终止循环的执行, 即循环代码遇到 break,就不再循环了
	continue 是结束本次循环,继续下一次循环, 即本次循环剩下的代码不再执行,但会进行下一次循环

'''

for i in range(10):
    if i % 5 == 0:
        continue
    print(i,end=" ")    # 1 2 3 4 6 7 8 9
print()


for i in range(1, 10):
    if i % 5 == 0:
        break
    print(i,end=" ")    # 1 2 3 4
print()