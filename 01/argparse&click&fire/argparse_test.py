import argparse


def parse_opt():
    parser = argparse.ArgumentParser()
    parser.add_argument('--data', type=str, default='data/coco128.yaml', help='dataset.yaml path')
    parser.add_argument('--weights', nargs='+', type=str, default='yolov5s.pt', help='model.pt path(s)')
    parser.add_argument('--batch-size', type=int, default=1, help='batch size')
    parser.add_argument('--device', default='cpu', choices=["cpu", "cuda"], help='cuda or cpu')
    parser.add_argument('--half', action='store_true', help='FP16 half-precision export')
    parser.add_argument('--conf-thres', type=float, default=0.25, help='TF.js NMS: confidence threshold')
    parser.add_argument(
        '--include',
        nargs='+',
        default=['torchscript'],
        help='torchscript, onnx, openvino, engine, coreml, saved_model, pb, tflite, edgetpu, tfjs, paddle')
    opt = parser.parse_args()
    return opt


if __name__ == '__main__':
    opt = parse_opt()
    print(opt)
    # > python argparse_test.py --data coco.yaml --weights yolov5x.pt --batch-size 16 --device cuda --half --conf-thres 0.5 --include onnx
    # Namespace(data='coco.yaml', weights=['yolov5x.pt'], batch_size=16, device='cuda', half=True, conf_thres=0.5, include=['onnx'])
