'''
input 必须以 r rb rU U 模式打开,只能读取,不能写入

fileinput.input() 可以同时读取多个文件

fileinput.input (files='filename', inplace=False, backup='', bufsize=0, mode='r', openhook=None)
    - files:         # 文件的路径列表，默认是stdin方式，多文件['1.txt','2.txt',...]
    - inplace:       # 是否将标准输出的结果写回文件，默认不取代
    - backup:        # 备份文件的扩展名，只指定扩展名，如.bak。如果该文件的备份文件已存在，则会自动覆盖。
    - bufsize:       # 缓冲区大小，默认为0，如果文件很大，可以修改此参数，一般默认即可
    - mode:　　　　　  # 读写模式，默认为只读
    - openhook:　　　 # 该钩子用于控制打开的所有文件，比如说编码方式等;
'''

from fileinput import input

path = ['./fileinput1.txt', './fileinput2.txt']

with input(files=path, mode='r') as files:
    # 读取一行
    res = files.readline()
    print(res, end='')      # aaaaaa
    res = files.readline()
    print(res, end='')      # bbbbbb

    # 剩余的行
    lines = list(files)
    print(lines)            # ['cccccc\n', 'dddddd\n', 'eeeeee\n', 'ffffff\n', 'gggggg\n', 'hhhhhh\n', 'iiiiii\n', 'jjjjjj\n', 'kkkkkk\n', 'llllll\n']
