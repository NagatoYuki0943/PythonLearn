num = 1


def func():
    print("my_module1 func")


class Dog(object):
    def __init__(self, name):
        self.name = name

    @staticmethod
    def show_info():
        print("my_module1 Dog class")