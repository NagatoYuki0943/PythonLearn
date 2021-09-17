'''
python,js,php可以再类外添加(删除)属性
不同对象之间的属性值没关联
直接使用 . 即可,没有就添加,有就修改
dog.name = '汪汪'
dog.age = 2

删除属性
del 对象.属性
'''

class Dog(object):
    def play(self):
        print('小狗咬人了')


dog = Dog()

# 外部给对象添加属性
dog.name = '汪汪'
dog.age = 2
print(dog.name, f'{dog.age}岁')  # 汪汪 2岁


# 修改属性值
dog.age = -1
print(dog.name, f'{dog.age}岁')  # 汪汪 -1岁


dog1 = Dog()
dog1.sex = 'male'
print(dog1.sex)


# 删除数据
del dog1.sex

