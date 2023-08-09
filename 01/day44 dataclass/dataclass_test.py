from dataclasses import dataclass, field


@dataclass
class Config:
    det_model: str                              # Path of Detection model of PPOCR.
    cls_model: str                              # Path of Classification model of PPOCR.
    rec_model: str                              # Path of Recognization model of PPOCR.
    rec_label_file: str                         # Path of Recognization label of PPOCR.
    device: str                                 # Type of inference device, support 'cpu' or 'gpu'.
    cls_bs: int                                 # Classification model inference batch size.
    rec_bs: int                                 # Recognition model inference batch size
    # default 必须放在最后面
    device_id: int | None = None                # Define which GPU card used to run model.
    backend: str  = field(default="default")    # Type of inference backend, support ort/trt/paddle/openvino, default 'openvino' for cpu, 'tensorrt' for gpu


def parse_arguments():
    config = Config(
        det_model = r"ch_PP-OCRv3_det_infer",
        cls_model = r"ch_ppocr_mobile_v2.0_cls_infer",
        rec_model = r"ch_PP-OCRv3_rec_infer",
        rec_label_file = r"ppocr_keys_v1.txt",
        device = "cpu",
        cls_bs = 1,
        rec_bs = 6,
        # device_id = 0,
        # backend = "default",
    )
    return config


# __post_init__
# 类在初始化的时候传入了两个值（或者多个值），但是根据这两个值会自动可以确认第三个值，我不希望再单独调用后生成第三个值。
# 即： 我期望在我给初始化传入两个值后，完成初始化动作后，第三个值自动生成了。
@dataclass
class C:
    a: float
    b: float
    c: float = field(init=False)    # 不需要初始化

    def __post_init__(self):
        self.c = self.a + self.b


def test_post_init():
    c1 = C(10, 20)
    print(f"c1:{c1}")
    # c1:C(a=10, b=20, c=30)


# 这个参数在对象初始化后，会禁止更改值
@dataclass(frozen=True)
class Data:
    name: str
    value: int = 42


def test_frozen():
    data = Data('my_name', 99)
    data.name = 'other'  # 报错：cannot assign to field 'name'


if __name__ == "__main__":
    print(parse_arguments())
    # Config(det_model='ch_PP-OCRv3_det_infer', cls_model='ch_ppocr_mobile_v2.0_cls_infer', rec_model='ch_PP-OCRv3_rec_infer', rec_label_file='ppocr_keys_v1.txt', device='cpu', cls_bs=1, rec_bs=6, device_id=None, backend='default')

    test_post_init()
    test_frozen()
