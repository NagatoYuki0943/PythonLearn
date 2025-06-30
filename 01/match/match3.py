# match case 不会区分序列的类型，对 tuple 和 list 都会匹配成功


my_tp = (0, 0)
my_lst = [0, 0]


match my_tp:
    case [0, 0]:
        print("Matched tuple t with square brackets")


match my_lst:
    case (0, 0):
        print("Matched list l with parentheses")


match my_lst:
    case 0, 0:
        print("Matched list l with no brackets")


# 如果关心类型，要用下面的写法
match my_tp:
    case tuple([0, 0]):
        print("Matched tuple t with tuple constructor")
    case list([0, 0]):
        print("Matched list l with list constructor")


match my_lst:
    case tuple([0, 0]):
        print("Matched tuple t with tuple constructor")
    case list([0, 0]):
        print("Matched list l with list constructor")


# 如果只关心类型，用下面的写法
match my_tp:
    case tuple():
        print("Matched tuple t with tuple constructor")
    case list():
        print("Matched list l with list constructor")

print("-" * 20)


def check_empty_sequence1(data):
    match data:
        case list():
            print("这是一个空的列表")
        case tuple():
            print("这是一个空的元组")
        case [*_]:
            print("这是一个非空序列")
        case _:
            print("这不是一个列表或元组")


check_empty_sequence1([])  # 这是一个空的列表
check_empty_sequence1(())  # 这是一个空的元组
check_empty_sequence1([1])  # 这是一个非空序列
check_empty_sequence1((2, 3))  # 这是一个非空序列
check_empty_sequence1({})  # 这不是一个列表或元组
print("-" * 20)


def check_empty_sequence2(data):
    match data:
        case list() | tuple():
            print("这是一个空的列表或元组")
        case [*_]:
            print("这是一个非空序列")
        case _:
            print("这不是一个列表或元组")


check_empty_sequence2([])  # 这是一个空的列表或元组
check_empty_sequence2(())  # 这是一个空的列表或元组
check_empty_sequence2([1])  # 这是一个非空序列
check_empty_sequence2((2, 3))  # 这是一个非空序列
check_empty_sequence2({})  # 这不是一个列表或元组
