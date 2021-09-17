'''
组包: 将多个数据值给一个变量
拆包: 将容器中的数据分别给到多个变量,变量数量和数据数量一致
list拆包获取的值
dict拆包获取的key

es6中的数组和对象结构类似,不过不要求数量相等,不要的地方可以使用逗号占位,还可以使用默认值
let info1 = ['Mr Lee', 100, '男'];
let [name1, age1, gender1] = info1;
//3. 数组也能用() ,防止重复声明问题
([name3, age3, gender3] = ['Miss Liu', 102, '女']);
//4. 数组层次也需要匹配
let [name4, [age4, gender4]] = ['Mr.Qian', [15, 'male']];
//5. 用逗号作为占位符不赋值
let [, , gender5] = ['Mr.Lee', 100, '男'];
//6. 在变量解构时，可以在数组的元素中设置一个默认值；
let [name6, age6, gender6 = 'female'] = ['Miss.Zhang', 11];
//7. 还有一种...var 的语法，可以将没有赋值的内容都赋值给这个变量,形成一个数组；
let [name7, ...other7] = ['Mr Hai', 100, 'fff'];

//对象解构
let obj8 = {
    name8: 'Me',
    age8: 100
};
let { name8, age8 } = obj8; //赋值的变量名要和对象中的名字相同
//4. 如果不想要对象属性名作为解构变量，可以通过键值对的方式更改变量名；  前边是原名,后面的是自定义名字
let obj11 = {
    name11: 'Aca',
    age11: 526
};
let { name11: MyName, age11: MyAge } = obj11;
//5. 对象解构不需要的部分不需要占位
let obj12 = {
    name12: 'SSSS',
    age12: 156
};
//只要age不要姓名
let { age12 } = obj12;
'''

# 组包: 将多个数据值给一个变量
a = 1, 2, 3
print(a)            # (1, 2, 3)


def func():
    return 1, 2     # 组包


# 拆包
x, y, z  =a
print(x, y, z)      # 1 2 3
x, y = func()
print(x, y)         # 1 2


# list拆包
[a, b] = [10, 20]
print(a, b)         # 10 20
a, b = [30, 40]
print(a, b)         # 30 40


# dict拆包获取key值
name, age = {'name':'Tom', 'age':5}
print(name, age)    # name age


# 交换两个变量的值
a = 11
b = 22
[a, b] = [b, a]
print(a, b)         # 22 11

