'''
拆包补充 使用 *args和 **kwargs 获取list和dict

拆包使用 * , 类似于ES6中的 [...array]
将列表中的每一个数据当做位置参数进行传递
list = [1, 2, 3, 4, 5, 6]
*list       通过 *args获取

将字典进行传递
一个 * 传递的是key
*dict,      通过 *args获取
两个 * 传递的是键值对
+**dict     通过 **kwargs获取

'''


def func(*args, **kwargs):
    print('args', args)
    print('kwargs', kwargs)
    print('*' * 50)


list = [1, 2, 3, 4, 5, 6]
dict = {'a': 7, 'c': 8, 'b': 9, 'd': 10}


# 列表拆包使用 * , 类似于ES6中的 [...array]
# 将列表中的每一个数据当做位置参数进行传递
func(*list)
# args (1, 2, 3, 4, 5, 6)
# kwargs {}


# 直接使用字典会报错
#func(dict1)

# 一个 * 传递的是key
func(*dict)
# args ('a', 'c', 'b', 'd')
# kwargs {}


# 两个 * 传递的是键值对
func(**dict)
# args ()
# kwargs {'a': 7, 'c': 8, 'b': 9, 'd': 10}
