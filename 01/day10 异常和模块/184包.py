'''
包: 功能相近或者相似的模块放在一个目录中,并在目录中定义一个 __init__.py 文件,这个目录就是包

导入模块
    方法1  import 包名.模块名

    方法2  from 包名 import 模块名

导入功能
    方法3  from 包名.模块 import 功能名

    方法4  from 包名.模块 import *

导入 __init__.py中的内容
    方法5  from 包名 import *

as 起别名  使用as之后别名就不能使用了,可以对模块,属性,方法,对象起别名
'''

# 方法1  import 包名.模块名
import package184.my_module1 as mm1

print(mm1.num)  # 10
mm1.func()      # 184 my_module1 func


# 方法2  from 包名 import 模块名
from package184 import my_module1
my_module1.func()


# 方法3  from 包名.模型 import 功能
from package184.my_module2 import func
func()          # 184 my_module2 func


# 方法4  from 包名.模型 import *
from package184.my_module2 import *
print(num)      # 20


# 方法5  from 包名 import *  导入的是 __init__.py中的内容
from package184 import *
func()          # package184 init func

