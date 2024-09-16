"""
":=" 运算符的主要用途是在条件语句、循环语句或其他表达式中为变量赋值，同时使用该变量的值。下面是一些示例：
"""

users: dict[int, str] = {0: "Bob", 1: "Mario"}

user: str | None = users.get(3)
if user:
    print(f"{user} exists!")
else:
    print("User not found!")
# User not found!

# 更简单的写法
if user := users.get(3):
    print(f"{user} exists!")
else:
    print("User not found!")
# User not found!


def get_info(text: str) -> dict:
    # 直接生成变量
    return {
        "words": (words := text.split()),
        "word_count": len(words),
        "character_count": len("".join(words)),
    }


print(get_info("hello"))
# {'words': ['hello'], 'word_count': 1, 'character_count': 5}


my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# 在 if 语句中使用赋值表达式：
if (n := len(my_list)) > 10:
    print(f"List is too long ({n} elements, expected <= 10)")
# List is too long (11 elements, expected <= 10)


# 在 while 循环中使用赋值表达式：
while num := my_list[-1]:
    print(num, end=" ")
    my_list.pop(-1)
print()
# 10 9 8 7 6 5 4 3 2 1 没有0,因为0会被判断为False


# 在列表推导式中使用赋值表达式：
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_list1 = [num1 for num in my_list if (num1 := num * 2)]
print(my_list1)
# [2, 4, 6, 8, 10, 12, 14, 16, 18, 20] 没有0,因为0会被判断为False
