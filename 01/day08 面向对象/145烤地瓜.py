"""
字符串,join(列表)
可以将列表使用字符串分隔开,返回一个字符串
"""


class Potato(object):
    def __init__(self):
        self.status = "生的"
        self.status = ""
        self.total_time = 0
        self.seasoning = []

    def cock(self, time):
        # 计算总时间
        self.total_time += time
        # 修改地瓜状态
        if self.total_time < 3:
            self.status = "生的"
        elif self.total_time < 6:
            self.status = "不熟"
        elif self.total_time < 8:
            self.status = "熟了"
        else:
            self.status = "糊了"

    def add(self, *args):
        """
        添加调料
        """
        for i in args:
            self.seasoning.append(i)

    def __str__(self):
        if self.seasoning:
            # 字符串.join(列表), 列表使用字符串连接
            temp = ",".join(self.seasoning)

            return (
                f"地瓜状态: {self.status},烧烤总时间:{self.total_time}分钟,调料: {temp}"
            )
        else:
            return f"地瓜状态: {self.status},烧烤总时间:{self.total_time}分钟,没调料"


potato = Potato()
print(potato)  # 地瓜状态: 生的,烧烤总时间:0分钟,没调料
potato.cock(4)
potato.add("油")
print(potato)  # 地瓜状态: 不熟,烧烤总时间:4分钟,调料: 油
potato.cock(3)
potato.add("孜然")
print(potato)  # 地瓜状态: 熟了,烧烤总时间:7分钟,调料: 油,孜然
potato.cock(2)
potato.add("辣椒", "胡椒")
print(potato)  # 地瓜状态: 糊了,烧烤总时间:9分钟,调料: 油,孜然,辣椒,胡椒
