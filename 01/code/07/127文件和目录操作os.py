'''
对文件和目录的操作,需要导入os模块
1.文件[夹]重命名   os.rename(原文件路径名,新文件路径名)
    文件不存在会报错

  创建文件使用 open(路径名,'w')  w模式不存在文件就会创建
2.删除文件    os.remove(文件路径名)
    文件不存在会报错

3.创建目录    os.mkdir(目录路径名) make directory
    目录存在会报错
    新建多层目录要保证外层目录存在

4.删除空目录   os.rmdir(目录路径名) remove directory
    目录不为空和不存在都报错

5.获取当前所在的目录  os.getcwd()  get current working directory


6.修改当前的目录     os.chdir(目录名)  change dir
    目录不存在会报错

7.获取指定目录中的内容 os.listdir(目录)   默认不写参数获取当前路径名
  返回值是列表,列表中的每一项是文件名


8.判断文件是否存在 os.path.exists(文件路径)
    存在返回True,不存在返回False
'''
import os


# 1.文件[夹]重命名   os.rename(原文件路径名,新文件路径名)
# 文件不存在会报错
#os.rename('文件/4.txt', '文件/4.txt')


# 2.删除文件    os.remove(文件路径名)
# 文件不存在会报错
#os.remove('文件/4.txt')


# 3.创建目录    os.mkdir(目录路径名) make directory
# 目录存在会报错
#os.mkdir('dir')
# 在dir目录中再创建一个目录,前提是dir目录存在
#os.mkdir('dir/a')


# 4.删除空目录   os.rmdir(目录路径名) remove directory
# 目录不为空和不存在都报错
#os.rmdir('dir/a')


# 5.获取当前所在的目录  os.getcwd()  get current working directory
dir = os.getcwd()
print(dir)      # D:\Python\Pycharm\01\code\07


# 6.修改当前的目录     os.chdir(目录名)  change dir
# 目录不存在会报错
os.chdir('文件')
dir = os.getcwd()
print(dir)      # D:\Python\Pycharm\01\code\07\dir


# 7.获取指定目录中的内容 os.listdir(目录)   默认不写参数获取当前路径名
#   返回值是列表,列表中的每一项是文件名
os.chdir('../')
res = os.listdir()
print(res)
# ['122文件的读操作read([n]).py', '123文件按行读取readline[s].py'...
os.chdir('文件')
res = os.listdir()
print(res)
os.chdir('../')
# ['1.txt', '2.txt', '3.m', '4.txt', 'back.txt', 'forward.txt']


# 8.判断文件是否存在 os.path.exists(文件路径)
exists = os.path.exists('文件/1.txt')
print(exists)   # True

