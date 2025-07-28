# 两个完全相同的集合
set1 = {1, 2, 3, 4}
set2 = {4, 3, 2, 1} # 顺序不同，但元素相同

# 两个不相同的集合
set3 = {1, 2, 3}
set4 = {1, 2, 5}

# 比较结果
print(f"set1 和 set2 是否相同? {set1 == set2}") # True
print(f"set1 和 set3 是否相同? {set1 == set3}") # False
print(f"set3 和 set4 是否相同? {set3 == set4}") # False
print(f"set1 和 set2 是否不同? {set1 != set2}") # False
print(f"set1 和 set3 是否不同? {set1 != set3}") # True
print(f"set3 和 set4 是否不同? {set3 != set4}") # True
