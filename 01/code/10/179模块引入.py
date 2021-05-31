'''
注意点: 如果导入的是自己书写的模块,使用的模块和代码文件需要在一个目录中,不然要写路径
注意: 如果存在同名方法会被替换

方法1
引入全部
引入:    import 模块名
使用:    模块名.功能名


方法2
引入具体功能
引入: form 模块名 import 功能名
使用: 功能名


方法3
将模块中所有功能全部引入 不建议用
引入: from 模块名 import *
使用: 功能名


as 起别名  使用as之后别名就不能使用了,可以对模块,属性,方法,对象起别名
'''


# 方法1
# 引入:    import 模块名
# 使用
import my_module1
# 调用
print(my_module1.num)            # 1
my_module1.func()                # # my_module1 func
dog = my_module1.Dog('小黄')
my_module1.Dog.show_info()       # my_module1 Dog class



# 方法2
# 引入: form 模块名 import 功能名
from my_module2 import func     # my_module2 func
func()



# 方法3
# 引入: from 模块名 import *
from my_module3 import *
print(num)                      # 3



# as 起别名  使用as之后别名就不能使用了,可以对模块,属性,方法,对象起别名
import my_module3 as mm1

mm1.func()                      # my_module3 func

from my_module2 import num as number
print(number)                   # 2

