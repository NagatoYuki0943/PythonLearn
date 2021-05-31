'''
对象.__dict__  查看对象具有的属性,类型是字典,key是属性名,value是属性值
print(xw.__dict__)  # {'_People__ICBC_money': 0}

类.__dict__  查看类具有的属性,类型是字典,key是属性名,value是属性值


就是其他语言的 private
python中的私有本质是修改属性/方法的名字,在属性/方法前面添加 _类名 前缀,如 _People__ICBC_money

访问权限控制: 在什么地方可以使用和操作.
私有权限:
	定义: 在方法和属性前加上两个下划线, 就变为私有.  __sex_hobby
	1. 不能在类外部通过对象直接访问和使用, 只能在类内部访问和使用
	2. 不能被子类继承,
公有: 不是私有的,就是公有的.
'''

# 定义People类,定义属性 money ,不能随意被修改,要用合法方法修改
class People(object):


    def __init__(self):
        self.__ICBC_money = 0


    def setMoney(self, money):
        self.__ICBC_money = money


    def get_money(self):
        print(f"钱:{self.__ICBC_money}")


xw = People()
print(xw.__dict__)  # {'_People__ICBC_money': 0}

# 添加公有属性,不是修改私有属性
xw.__ICBC_money = 200
print(xw)           # 钱:0,虽然上面添加了100,但是那是新添加的公有属性,不是类内的私有属性
print(xw.__dict__)  # {'_People__ICBC_money': 0, '__ICBC_money': 200}


xw.setMoney(100)
xw.get_money()      # 钱:100
print(xw.__dict__)  # {'_People__ICBC_money': 100, '__ICBC_money': 100}

# 查看类的属性
print(People.__dict__)