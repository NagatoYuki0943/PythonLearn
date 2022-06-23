#------------------------------------------#
#   getattr() 函数用于返回一个对象属性值
#   getattr 语法：
#       getattr(object, name[, default])
#   参数
#       object  -- 对象
#       name    -- 字符串，对象属性
#       default -- 默认返回值，如果不提供该参数，在没有对应属性时，将触发 AttributeError
#
#   getattr可以在类中使用，参数1为self，获取对象参数
#------------------------------------------#


class Person(object):
    inherit = 'DNA'
    def __init__(self, age) -> None:
        self.age = age

# 可以获取 类变量 和 实例变量
person = Person(12)
print(getattr(person, 'inherit'))       # DNA
print(getattr(person, 'age'))           # 12
print(getattr(person, 'name', 'may'))   # may
print('\n')


class Calc(object):
    def add(self, *args):
        return sum(args)

    def sub(self, *args):
        res = args[0]
        for i in args[1:]:
            res -= i
        return res

    def mul(self, *args):
        res = args[0]
        for i in args[1:]:
            res *= i
        return res

    def div(self, *args):
        res = args[0]
        for i in args[1:]:
            assert i != 0, f"second argument {i} can't be zero"
            res /= i
        return res

clac = Calc()
a = [4, 3, 2, 1]

print(clac.add(*a))     # 10
print(clac.sub(*a))     # -2
print(clac.mul(*a))     # 0
print(clac.div(*a))     # 0.6666666666666666
print('\n')

#------------------------------------------#
#   getattr获取的方法可以直接使用
#------------------------------------------#
add = getattr(clac, 'add')
sub = getattr(clac, 'sub')
mul = getattr(clac, 'mul')
div = getattr(clac, 'div')
print(add(*a))          # 10
print(sub(*a))          # -2
print(mul(*a))          # 0
print(div(*a))          # 0.6666666666666666


#------------------------------------------#
#   getattr可以在类中使用，参数1为self，获取对象参数
#------------------------------------------#
class Coordinate():
    x = 10
    y = -5
    def __init__(self):
        self.z = 0

    def get(self):
        x = getattr(self, 'x', -1)
        z = getattr(self, 'z', -1)
        a = getattr(self, 'a', -1)
        print(x, z, a)

point1 = Coordinate()
point1.get()            # 10 0 -1
