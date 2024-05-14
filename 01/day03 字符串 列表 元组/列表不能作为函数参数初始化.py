import copy



arr1 = [[1, 2, 3], [4, 5, 6]]
# 默认浅拷贝
arr2 = arr1
# 这里修改arr2,同时修改了arr1
arr2[0][0] = 100
print(arr1)
# [[100, 2, 3], [4, 5, 6]]


arr1 = [[1, 2, 3], [4, 5, 6]]
# 使用 [:] 赋值也是浅拷贝
arr2 = arr1[:]
# 这里修改arr2,同时修改了arr1
arr2[0][0] = 100
print(arr1)
# [[100, 2, 3], [4, 5, 6]]


arr1 = [[1, 2, 3], [4, 5, 6]]
# 默认浅拷贝
arr2 = arr1.copy()
# 这里修改arr2,同时修改了arr1
arr2[0][0] = 100
print(arr1)
# [[100, 2, 3], [4, 5, 6]]


arr1 = [[1, 2, 3], [4, 5, 6]]
# 使用深拷贝可以避免上面的问题
arr2 = copy.deepcopy(arr1)
# 这里只修改arr2
arr2[0][0] = 100
print(arr1)
# [[1, 2, 3], [4, 5, 6]]


"""
给函数变量设置可变类型默认参数会产生意外的状况
"""
def add_fruit(fruit, fruits: list = []):
    fruits.append(fruit)
    print(fruits)

add_fruit('apple')  # ['apple']
add_fruit('orange') # ['apple', 'orange']
# 这里没有给函数传递第二个参数,列表中应该只有 organe,但是实际上还会有 apple
# 原因是python的默认参数在函数定义时就会被评估保存,而不是每次运行时才创建


# 正确写法,默认赋值为None,为None就在里面创建list
def add_fruit(fruit, fruits: list | None = None):
    fruits = [] if fruits is None else fruits
    fruits.append(fruit)
    print(fruits)

add_fruit('apple')  # ['apple']
add_fruit('orange') # ['orange']
