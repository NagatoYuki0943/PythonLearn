'''
函数名前面加上两个下划线改为私有方法
python中的私有本质是修改属性/方法的名字,在属性/方法前面添加 _类名 前缀,如 _People__ICBC_money
'''

class Dog(object):
    def born(self):
        '''生小狗,生一个小狗,休息30天'''
        print("生了一个小狗")
        self.__sleep()


    def __sleep(self):
        print("休息30天")


dog = Dog()
#dog.__sleep()   # 报错

print(dog.__dict__)     # {}