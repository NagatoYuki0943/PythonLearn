import student
import os


class StudentManagerSystem(object):
    def __init__(self):
        # 这里使用字典保存,
        self.__stu_dicts = {}

    # 显示菜单
    @staticmethod
    def __show_menu():
        '''
        展示菜单
        '''
        print('1.添加学生')
        print('2.删除学生')
        print('3.修改学生')
        print('4.查询单个信息')
        print('5.查询所有信息')
        print('6.删除全部信息')
        print('7.退出')

    # 开始界面
    def start(self):

        # 读取文件信息
        self.__open_file()

        while True:
            self.__show_menu()
            opt = input('请输入编号:')

            if opt == "1":
                self.__insert_student()
            elif opt == "2":
                self.__remove_student()
            elif opt == "3":
                self.__modify_student()
            elif opt == "4":
                self.__search_student()
            elif opt == "5":
                self.__show_all_info()
            elif opt == "6":
                self.__del_all()
            elif opt == "7":
                print('欢迎下次使用')
                self.__save()
                break
            else:
                print('输入有误,请再次输入')
                continue  # 不用再按回车

            input('*****请按回车键继续*****')

    # 添加学生信息
    def __insert_student(self):
        # 使用input获取学生信息
        id = input("请输入学生学号:")
        # 代码优化,判断学号是否存在  in 判断key值是否在字典中
        if id in self.__stu_dicts:
            #key 存在
            print("学生信息已经存在,不能再次添加,可以修改")
            return

        name = input("请输入学生姓名:")
        age = input("请输入学生年龄:")
        gender = input("请输入学生性别:")

        # 2.使用学生信息,创建学生对象
        stu = student.Student(id, name, age, gender)

        # 3.将学生对象添加到字典
        self.__stu_dicts[id] = stu

    # 删除学生信息
    def __remove_student(self):
        # 删除学生信息
        id = input("请输入要删除的学生学号:")
        if id in self.__stu_dicts:
            #del self.__stu_dicts[id]
            self.__stu_dicts.pop(id)
            print("学生已经删除")
        else:
            print("学生信息不存在")

    # 修改学生信息
    def __modify_student(self):
        # 修改学生信息
        id = input("请输入要修改的学生学号:")
        if id in self.__stu_dicts:
            # 用变量保存,可以直接修改原值
            stu = self.__stu_dicts[id]
            stu.name = input("请输入新姓名:")
            stu.age = input("请输入新年龄:")
            stu.gender = input("请输入新性别:")
            print("学生信息修改完毕")
        else:
            print("学生信息不存在")

    # 查找学生信息
    def __search_student(self):
        # 查找学生信息
        id = input("请输入要修改的学生学号:")
        if id in self.__stu_dicts:
            print(self.__stu_dicts[id])
        else:
            print("学生信息不存在")

    # 显示所有学生信息
    def __show_all_info(self):
        if self.__stu_dicts:
            for stu in self.__stu_dicts.values():
                print(stu)
        else:
            print("没学生")

    # 删除全部信息
    def __del_all(self):
        flag = input("确认删除请输入yes:")
        if flag == "yes":
            self.__stu_dicts.clear()
            print("全部信息删除成功")

    # __stu_dicts 存放的是对象地址,所以要存储具体的对象信息,通过遍历存储
    def __save(self):
        # 写文件方式打开文件,不存在就创建
        f = open("student.txt", "w", encoding="utf-8")

        # 保存学生的信息,要写上 values()
        for stu in self.__stu_dicts.values():
            f.write(str(stu) + "\n")   # str(stu)会调用 student类中的 __str()__ 方法

    # 读取学生信息
    def __open_file(self):
        try:
            # 文件存在才提取
            if os.path.exists("student.txt"):
                f = open("student.txt", "r", encoding="utf-8")
                # 1.读取所有行,返回列表
                buffer_list = f.readlines()

                # 2.去除换行符
                buffer_list = [i.strip() for i in buffer_list]

                # 3.split取出所有的信息,放进对象
                for i in buffer_list:
                    id, name, age, gender = i.split(",")
                    #print(id, name, age, gender)    # 2 a 34 male

                    # 4.创建学生对象
                    stu = student.Student(id, name, age, gender)

                    # 5.添加进学生dict中
                    self.__stu_dicts[id] = stu
        except Exception as e:
            print(e)
