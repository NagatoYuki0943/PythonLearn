class Student(object):
    def __init__(self, id, name, age, gender):
        self.stu_id = id
        self.name = name
        self.age = age
        self.gender = gender


    def __str__(self):
        return f"{self.stu_id},{self.name},{self.age},{self.gender}"


# 只有自己执行才会执行里面的内容
if __name__ == '__main__':
    stu = Student(1, 'a', 18, 'male')
    print(stu)