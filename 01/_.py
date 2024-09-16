shape = [1, 3, 224, 224]


b, c, h, w = shape
print(b, c, h, w)  # 1 3 224 224


b, *_ = shape
print(b)  # 1
print(_)  # [3, 224, 224]
