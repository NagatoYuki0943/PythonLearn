from typing import Any

class Test(object):

    def __init__(self) -> None:
        super().__init__()
        print("__init__")


    def run(self):
        print("正在疯跑")


    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        print('__call__')


test = Test()
test()