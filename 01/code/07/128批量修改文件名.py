'''
创建文件直接使用 open(文件名, 'w')  w 写入模式,不存在就创建
'''
import os


def create_files_1():
    '''
    批量创建文件
    '''
    for i in range(10):
        file_name = 'file_' + str(i) + '.txt'
        # w 模式打开文件,文件不存在就创建新的
        f = open('批量修改文件名/' + file_name, 'w')


#create_files_1()


def create_files_2():
    '''
    批量创建文件
    '''
    os.chdir('批量修改文件名/')
    for i in range(10, 20):
        file_name = 'file_' + str(i) + '.txt'
        # w 模式打开文件,文件不存在就创建新的
        f = open(file_name, 'w')
    os.chdir('../')


#create_files_2()


def modify_filename():
    '''
    批量修改文件名
    '''
    os.chdir('批量修改文件名/')
    # 获取所有文件
    buffer = os.listdir()

    for file in buffer:
        #newfile = 'py_' + file
        newfile = file[3::]
        os.rename(file, newfile)
    os.chdir('../')


# modify_filename()


def rename():
    os.chdir('批量修改文件名')
    buffer = os.listdir()
    for old in buffer:
        #new = 'py_' + old
        new = old[3::]
        os.rename(old, new)
    os.chdir('../')


rename()



