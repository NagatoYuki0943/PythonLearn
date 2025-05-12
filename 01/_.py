shape = [1, 3, 224, 224]


b, c, h, w = shape
print(b, c, h, w)  # 1 3 224 224
print()


b, *_ = shape
print(b)  # 1
print(_)  # [3, 224, 224]
print()


b, *_, h = shape
print(b, h)  # 1 224
print(_)  # [3, 224, 224]
print()


*_, h, w = shape
print(_)  # [1, 3]
print(h, w)  # 224 224
print()
