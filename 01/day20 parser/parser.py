'''
运行文件时的参数
`D:\Anaconda3\envs\ai\python.exe C:/Ai/YOLO/PyTorch-YOLOv3/train.py --data_config config/coco.data --pretrained_weights weights/darknet53.conv.74`
指定参数 用空格或者等于号都可以
    --data_config config/coco.data					# coco数据集
    --pretrained_weights weights/darknet53.conv.74	# 载入预训练权重

可以指定没有 -- 的参数
    例如：
        parser.add_argument("--epochs")
        在写的时候不用 epoch 100 ,直接写100, 写了 epoch 会报错
'''


import argparse

if __name__ == "__main__":
    # 初始化参数
    parser = argparse.ArgumentParser()
    parser.add_argument("--epochs",                 type=int, default=100,  help="number of epochs")
    parser.add_argument("--batch_size",             type=int, default=4,    help="size of each image batch")
    parser.add_argument("--gradient_accumulations", type=int, default=2,    help="number of gradient accums before step")
    parser.add_argument("--model_def",              type=str, default="config/yolov3.cfg", help="path to model definition file")
    parser.add_argument("--data_config",            type=str, default="config/coco.data", help="path to data config file")
    parser.add_argument("--pretrained_weights",     type=str,               help="if specified starts from checkpoint model")
    parser.add_argument("--n_cpu",                  type=int, default=0,    help="number of cpu threads to use during batch generation")
    parser.add_argument("--img_size",               type=int, default=416,  help="size of each image dimension")
    parser.add_argument("--checkpoint_interval",    type=int, default=1,    help="interval between saving model weights")
    parser.add_argument("--evaluation_interval",    type=int, default=1,    help="interval evaluations on validation set")
    parser.add_argument("--compute_map",            default=False,          help="if True computes mAP every tenth batch")
    parser.add_argument("--multiscale_training",    default=True,           help="allow for multi-scale training")
    # 添加为True,不写为False
    parser.add_argument("--openvino",               default=False, action="store_true", required=False, help="export openvino")
    opt = parser.parse_args()

    # 所有参数
    print(opt)
    # Namespace(batch_size=4, checkpoint_interval=1, compute_map=False,
    # data_config='config/coco.data', epochs=100, evaluation_interval=1,
    # gradient_accumulations=2, img_size=416, model_def='config/yolov3.cfg',
    # multiscale_training=True, n_cpu=0, pretrained_weights=None)

    print('*' * 50)

    # 获取指定参数
    batch_size = opt.batch_size
    print(batch_size)   # 4
    # 处理字符串
    print(opt.data_config.lower())
    # config/coco.data
