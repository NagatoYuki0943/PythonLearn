'''
try:
    可能发生异常的代码
excerpt Exception as e:
    发生异常执行的代码
    print(e)

else:
    代码没有发生异常才执行

finally:
    不管有没有发生异常都会执行

'''

while True:
    try:
        raise ValueError("Bad Value")
    except ValueError:
        print("break")
        break
    finally:
        # continue会覆盖break
        continue
# break
# break
# break
# ...