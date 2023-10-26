'''
math数据模块
'''

import math

# 幂操作
print(math.pow(2, 3))       #8.0

# 弧度值
print(math.sin(1.57))       #0.9999996829318346

# 弧度转角度
print(math.degrees(1.57))   # 89.95437383553924
print(math.degrees(3.1415926))
                            # 179.99999692953102

# 角度转弧度
print(math.radians(90))     # 1.5707963267948966
print(math.radians(30))     # 0.5235987755982988



# 向下取整
print(math.floor(4.9))      # 4
# 向上取整
print(math.ceil(4.1))       # 5
# 四舍五入
print(round(4.1))           # 4
print(round(4.5))           # 4
print(round(4.6))           # 5

