"""抽象基类
abc.ABC:            抽象基类
@abstractmethod:    抽象方法
@abstractproperty:  抽象属性
"""

from abc import ABC, abstractmethod


class Inference(ABC):
    # 抽象方法
    @abstractmethod
    def infer(self, x):
        raise NotImplementedError

try:
    inference = Inference()     # 在这一步就会报错
    inference.infer()
except Exception as error:
    print(error)        # Can't instantiate abstract class Inference with abstract method infer

# 不实现抽象方法会出错
class OrtInference(Inference):
    def __init__(self) -> None:
        super().__init__()

try:
    inference = OrtInference()  # 在这一步就会报错
    inference.infer()
except Exception as error:
    print(error)        # Can't instantiate abstract class OrtInference with abstract method infe

class PytorchInference(Inference):
    def __init__(self) -> None:
        super().__init__()

    def infer(self, x):
        print("Pytorch infer", x)

inference = PytorchInference()
inference.infer("1")    # Pytorch infer 1
