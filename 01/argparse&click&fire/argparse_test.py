import argparse


def parse_opt():
    parser = argparse.ArgumentParser()
    parser.add_argument('version', type=str, help='version, 必须在第一位,且不需要说明version')
    parser.add_argument('--weights', type=str, default='yolov5s.pt', help='model.pt path(s)')
    # default 代表不写 --device 参数时的默认值
    parser.add_argument('--device', default='cpu', choices=["cpu", "cuda"], help='cuda or cpu')
    # const 代表写 --evolve 但不写参数时的默认值
    parser.add_argument("--evolve", type=int, nargs="?", const=300, help="evolve hyperparameters for x generations")
    parser.add_argument('--half', action='store_true', help='FP16 half-precision export')
    parser.add_argument(
        '--include',
        nargs='+',  # n : 参数的绝对个数;  ? : 0或1个参数;  * : 0或所有参数;  + : 至少一个参数;
        default=['torchscript'],
        choices=["torchscript", "onnx", "openvino", "engine", "coreml", "saved_model", "pb", "tflite", "edgetpu", "tfjs", "paddle"],
        help='torchscript, onnx, openvino, engine, coreml, saved_model, pb, tflite, edgetpu, tfjs, paddle')
    opt = parser.parse_args()
    return opt


if __name__ == '__main__':
    opt = parse_opt()
    print(opt)
    # > python argparse_test.py v8 --weights yolov5x.pt --device cuda --evolve --include onnx   # 不指定--evolve
    # Namespace(version='v8', weights='yolov5x.pt', device='cuda', evolve=300, half=False, include=['onnx'])
    # > python argparse_test.py v8 --weights yolov5x.pt --evolve --include onnx                 # 不写--device
    # Namespace(version='v8', weights='yolov5x.pt', device='cpu', evolve=300, half=False, include=['onnx'])
