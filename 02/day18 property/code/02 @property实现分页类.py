'''
@property 把方法直接当做属性使用

类名: Page
方法:
    1.初始化方法
    2.获取开始位置
    3.获取结束位置


'''

class Page(object):
    # 1.初始化方法
    def __init__(self, number) -> None:
        # 当前页
        self.current_page = number

        # 每页大小
        self.page_size = 10

    
    # 2.获取开始位置
    @ property
    def start(self):
        # limit (当前页 - 1) * 每页大小, 
        # 1, 10
        # 11,20
        return (self.current_page - 1) * 10 + 1 # 从1开始


    # 3.获取结束位置
    @ property
    def end(self):
        return self.current_page * self.page_size


# 创建类的对象
page = Page(1)
print(page.start)
print(page.end)
