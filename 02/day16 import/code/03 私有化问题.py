'''
私有化使用的前提：必须使用 “ from xxx import *  “
用法： 在模块中，把变量前增加一个下划线 `_变量名`

注意：如果使用其他的方式导入模块，私有化将无效
    from xxx import _私有变量
    print(_私有变量)    不会报错

类里面的私有变量 两个下划线 __age
'''

from module import *
print(name) # Tom
print(_age) # 找不到