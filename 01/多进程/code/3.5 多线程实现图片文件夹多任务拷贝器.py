'''
只需要两行即可实现多线程

sub_thread = threading.Thread(target=copy_file, args=(file_name, source_dir, dest_dir))
sub_thread.start()
'''

import os
import threading


def copy_file(file_name, source_dir, dest_dir):
    '''
    复制文件
    file_name:  源文件名
    source_dir: 源文件夹路径
    dest_dir:   目标文件夹路径
    '''
    # 1 拼接源文件路径和目标文件路径
    source_path = os.path.join(source_dir, file_name)
    dest_path = os.path.join(dest_dir, file_name)

    # 2 打开源文件和目标文件
    with open(source_path, 'rb') as source_file:
        with open(dest_path, 'wb') as dest_file:
            # 3 循环读取源文件到目标路径
            while True:
                data = source_file.read(1024)
                if data:
                    dest_file.write(data)
                else:
                    break


if __name__ == '__main__':
    # 1 定义源文件夹和目标文件夹
    source_dir = r'D:\图片\hololive'
    dest_dir = r'C:\Users\Frostbite\Desktop\temp'

    # 2.创建目标文件夹
    try:
        os.mkdir(dest_dir)
    except:
        print("目标文件夹已经存在")    

    # 3.读取源文件夹的文件列表
    file_list = os.listdir(source_dir)
    
    for file_name in file_list:
        # 单线程模式
        # copy_file(file_name, source_dir, dest_dir)

        # 5.使用多线程实现多任务拷贝
        sub_thread = threading.Thread(target=copy_file, args=(file_name, source_dir, dest_dir))

        sub_thread.start()

    print('拷贝完毕')