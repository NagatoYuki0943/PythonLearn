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
