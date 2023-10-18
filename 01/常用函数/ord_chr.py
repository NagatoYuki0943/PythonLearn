"""
ord()函数主要用于将字符转换为整数，即获取ASCII给定字符的值；返回的结果是对应字符的ASCII码；

chr()函数是ord()函数的配对函数，主要用一个范围内的整数作参数，返回的结果是对应的字符，可以用十进制或者十六进制。
"""

num = ord('a')
print(num)      # 97
print(chr(num)) # a

for i in range(48, 58):
    print(chr(i), end = ' ')
print()
# 0 1 2 3 4 5 6 7 8 9

for i in range(65, 91):
    print(chr(i), end = ' ')
print()
# A B C D E F G H I J K L M N O P Q R S T U V W X Y Z

for i in range(97, 123):
    print(chr(i), end = ' ')
print()
# a b c d e f g h i j k l m n o p q r s t u v w x y z

for i in range(12):
    print(chr(9800 + i), end = "")
print()
# ♈♉♊♋♌♍♎♏♐♑♒♓
