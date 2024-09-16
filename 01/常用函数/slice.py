numbers: list[int] = list(range(1, 11))
text: str = "hello world"

print(numbers[::-1])  # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print(text[::-1])  # dlrow olleh

# 使用 slice 切片
rec: slice = slice(None, None, -1)
f_five: slice = slice(None, 5, None)
print(numbers[rec])  # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print(text[rec])  # dlrow olleh

print(numbers[f_five])  # [1, 2, 3, 4, 5]
print(text[f_five])  # hello
