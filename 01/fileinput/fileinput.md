# python文件处理之fileinput          

### 一、介绍

fileinput模块可以对一个或多个文件中的内容进行迭代、遍历等操作，我们常用的open函数是对一个文件进行读写操作。

fileinput模块的input()函数比open函数更高效和好用，体现在：

1. input()函数生成一个迭代器，保证了在遇到大文件的读取时不会占用太大的内存。
2. 用fileinput对文件进行循环遍历，格式化输出，查找、替换等操作，还能获取每一行的行号等等，非常方便。

 

### 二、fileinput.input() 可以同时读取多个文件

**input和FileInput完全相同,只是用法不同**

**input 必须以 r rb rU U 模式打开,只能读取,不能写入**

`fileinput.input (files='filename', inplace=False, backup='', bufsize=0, mode='r', openhook=None)`

- files:         # 文件的路径列表，默认是stdin方式，多文件['1.txt','2.txt',...]

- inplace:       # 是否将标准输出的结果写回文件，默认不取代
- backup:        # 备份文件的扩展名，只指定扩展名，如.bak。如果该文件的备份文件已存在，则会自动覆盖。
- bufsize:       # 缓冲区大小，默认为0，如果文件很大，可以修改此参数，一般默认即可
- mode:　　　　　# 读写模式，默认为只读
- openhook:　　　# 该钩子用于控制打开的所有文件，比如说编码方式等;



### 三、fileinput中的常用函数

| 函数                                | 描述                           |
| ----------------------------------- | ------------------------------ |
| input([files[, inplace[, backup]]]) | 帮助迭代多个输入流中的行       |
| filename()                          | 返回当前文件的名称             |
| lineno()                            | 返回（累计的）当前行号         |
| filelineno()                        | 返回在当前文件中的行号         |
| isfirstline()                       | 检查当前行是否是文件中的第一行 |
| isstdin()                           | 检查最后一行是否来自sys.stdin  |
| nextfile()                          | 关闭当前文件并移到下一个文件   |
| close()                             | 关闭序列                       |

**fileinput.input**是最重要的函数，它返回一个迭代器对象，如果要处理多个文件，可以向这个函数提供一个或多个文件名。

还可将参数inplace设置为True（inplace=True），对于你访问的每一行，都需打印出替代内容，这些内容将被写回到当前输入文件中，此时可选参数backup用于给从原始文件创建的备份文件指定扩展名。

```python
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
    
```



### 四.fileinput.Fileinput() 类 可以同时读取多个文件

**input和FileInput完全相同,只是用法不同**

**FileInput 必须以 r rb rU U 模式打开,只能读取,不能写入**

**FileInput可以使用fileinput中的大量方法**

```python
'''
FileInput 必须以 r rb rU 模式打开,只能读取,不能写入
FileInput可以使用fileinput中的大量方法
'''

import fileinput
from fileinput import FileInput

path = './fileinput1.txt'


# 将一个文件中所有的行提取到一个列表中
# files = list(FileInput(path))

print('open:')
with open(path, mode='r', encoding='utf-8') as files:
    lines = files.readlines()
    for line in lines:
        # 打印每一行
        print(line, end='')
print('*' * 50)



# FileInput可以同时打印多个文件
path = ['./fileinput1.txt', './fileinput2.txt']
files = FileInput(path, mode='r')
for l in list(files):
    # 打印每一行
    print(l, end='')
print('*' * 50)
# 读取一行
print(files.readline())
# 获取文件名
print(files.filename())
# files.filename()
```



