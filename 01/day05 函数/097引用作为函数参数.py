'''

函数传递的参数也是引用,
传递不可变类型不会改变原值,因为新值和旧值不同,引用不同了
传递可变类型会改变原值,list和dict中值也会被改变

直接使用全局变量,不可变类型不会被改变,除非使用global引入; 可变类型会被修改

+= 对于列表来说,类似于列表的extend方法,不会改变变量的引用地址,字典没有 +=

C++ 中数组作为函数参数,传递的是指针,因此可以直接修改原数组的值,和python中列表类似
'''

# 直接传递不可变类型,不会改变原值
num = 18
def func(a):
    a = a + 1
func(num)
print(num)  # 18


# 传递引用的list和dict会被修改
list1 = [1, 2, 3]
dict1 = {'name': 'Tom'}
def func1(a, b):
    a.append(4)
    b['name'] = 'Jerry'
    b['age'] = 5

func1(list1, dict1)
print(list1)        # [1, 2, 3, 4]
print(dict1)        # {'name': 'Jerry', 'age': 5}
print("*" * 50)


# 直接使用全局变量,不可变类型不会被改变; 可变类型会被修改
# 不使用global可以添加修改值,因为list中存放的是地址,可以直接修改,要修改list本身才要用 global,加上global也不会报错
list2 = [7, 9]
def func2():
    # 这个不算修改list,直接 = 赋值才是修改,要用global
    list2[0] = 15
    list2.append(10)
func2()
print(list2)    # [15, 9, 10]
print("*" * 50)


def func3():
    global list2
    list2 = [0, 0, 0]

func3()
print(list2)
print("*" * 50) #不加global [15, 9, 10]   加了global [0, 0, 0]


#  += 对于列表来说,类似于列表的extend方法,不会改变变量的引用地址,字典没有 +=
def func4(a):
    a += a

list3 = [1, 2, 3]
func4(list3)
print(list3)    # [1, 2, 3, 1, 2, 3]

