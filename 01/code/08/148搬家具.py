'''

'''

class Furniture(object):
    name = ''
    area = 0


    def __init__(self, name, area):
        self.name = name
        self.area = area


    def __str__(self):
        # 家具类型和占地面积
        return f"家具类型是{self.name},家具面积{self.area}平方米"


# 别墅
class Villa(object):


    def __init__(self, address, area):
        self.address = address
        self.area = area
        self.free_area = area   # 房子剩余面积
        self.furniture = []

    def add_furniture(self, *args):
        '''
        添加家具
        :param args: 必须是家具类对象
        '''
        for i in args:
            if self.free_area > i.area:
                # 添加家具
                self.furniture.append(i)
                # 更新剩余家具
                self.free_area -= i.area
                print(f"添加{i.name}成功")
            else:
                print(f"添加{i.name}失败")


    def __str__(self):
        if self.furniture:
            # 获取名字列表
            temp = [f"{i.name},面积是{i.area}平方米" for i in self.furniture]
            # 拼接字符串
            temp = ','.join(temp)
            return f"房子地址是{self.address},房子面积是{self.area}平方米,家具有{temp}"
        else:
            return f"房子地址是{self.address},房子面积是{self.area}平方米,没家具"


bed = Furniture("双人床", 6)
#print(bed)             # 家具类型是双人床,家具面积6平方米
desk = Furniture("桌子", 5)
chair = Furniture("椅子", 3)


villa = Villa('AAA',13)
print(villa)            # 房子地址是AAA,房子面积是13平方米,没家具

villa.add_furniture(bed, desk, chair)
# 添加双人床成功
# 添加桌子成功
# 添加椅子失败
print(villa)            # 房子地址是AAA,房子面积是13平方米,家具有双人床,面积是6平方米,桌子,面积是5平方米

