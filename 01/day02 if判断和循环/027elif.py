"""
if 	判断条件1:
    判断条件1成立,执行的代码
elif 判断条件2:
    判断条件1不成立,判断条件2 成立,会执行的代码
else:
    判断条件1和判断条件2都不成立,执行的代码
"""

score = input("请输入成绩:")

score = int(score)

if score > 90:
    print("优秀")
elif score > 80:
    print("正常")
else:
    print("再接再厉")
