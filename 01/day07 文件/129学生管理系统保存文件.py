"""
1.添加
2.删除
3.修改
4.查询单个信息
5.查询所有信息
6.退出
"""

import os

# 学生列表,下面直接使用即可,不用global引入,因为没有重新赋值,只是添加修改值
stu_list = []


def show_menu():
    """
    展示菜单
    """
    print("1.添加学生")
    print("2.删除学生")
    print("3.修改学生")
    print("4.查询单个信息")
    print("5.查询所有信息")
    print("6.退出")


def insert_student():
    """
    添加学生信息
    """
    # 1.获取学生信息
    name = input("请输入姓名:")

    for stu in stu_list:
        if stu["name"] == name:
            print("*****学生信息存在*****")
            return

    age = input("请输入年龄:")
    gender = input("请输入性别:")
    # 2.将学生信息添加到字典
    stu_dict = {"name": name, "age": int(age), "gender": gender}
    # 3.将字典添加到列表,不需要global,因为是添加,不是完整赋值
    stu_list.append(stu_dict)
    print("学生信息添加成功")


def show_all_info():
    """
    显示所有学生信息
    """
    if len(stu_list):
        print("姓名\t年龄\t性别")
        for stu in stu_list:
            print(stu["name"], "\t", stu["age"], "\t", stu["gender"])
    else:
        print("没学生")


def remove_student():
    # 1.获取学生姓名
    name = input("请输入要删除的学生的名字:")
    # 2.判断学生信息是否存在
    for stu in stu_list:
        # 3.学生信息存在,直接删除
        if stu["name"] == name:
            # 直接删除字典即可
            stu_list.remove(stu)
            print("*****删除成功*****")
            return
    # 4.学生信息不存在,直接结束
    else:
        print("*****该学生信息不存在*****")


def modify_student():
    # 1.获取学生姓名
    name = input("请输入要修改的学生的名字:")
    # 2.判断学生信息是否存在
    for stu in stu_list:
        # 3.学生信息存在,修改
        if stu["name"] == name:
            stu["age"] = input("请输入新的年龄:")
            stu["gender"] = input("请输入新的性别:")
            return
    # 4.学生信息不存在,直接结束
    else:
        print("*****该学生信息不存在*****")


def search_student():
    # 1.获取学生姓名
    name = input("请输入要显示的学生的名字:")
    # 2.判断学生信息是否存在
    for stu in stu_list:
        # 3.学生信息存在,修改
        if stu["name"] == name:
            print(stu["name"], "\t", stu["age"], "\t", stu["gender"])
            return
    # 4.学生信息不存在,直接结束
    else:
        print("*****该学生信息不存在*****")


def open_file():
    """
    查看学生信息
    """
    # 文件存在才打开,不存在就不管了,保存的时候会创建文件
    if os.path.exists("students/students.txt"):
        f = open("students/students.txt", "r", encoding="utf-8")
        buffer = f.read()

        # 数据存在才添加,不存在就不添加
        if buffer:
            # 要使用global引用全局变量
            global stu_list
            # 使用eval() 转换为原来的类型
            stu_list = eval(buffer)
            # print(stu_list, type(stu_list))
            f.close()


def save():
    """
    保存学生信息
    """
    f = open("students/students.txt", "w", encoding="utf-8")
    f.write(str(stu_list))
    f.close()


def main():
    # 加载文件
    open_file()

    while True:
        show_menu()
        opt = input("请输入编号:")

        if opt == "1":
            insert_student()
        elif opt == "2":
            remove_student()
        elif opt == "3":
            modify_student()
        elif opt == "4":
            search_student()
        elif opt == "5":
            show_all_info()
        elif opt == "6":
            print("欢迎下次使用")
            save()
            break
        else:
            print("输入有误,请再次输入")
            continue  # 不用再按回车

        input("*****请按回车键继续*****")


main()
