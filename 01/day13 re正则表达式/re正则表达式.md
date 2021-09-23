Python3 正则表达式

正则表达式是一个特殊的字符序列，它能帮助你方便的检查一个字符串是否与某种模式匹配。

re 模块使 Python 语言拥有全部的正则表达式功能。 

compile 函数根据一个模式字符串和可选的标志参数生成一个正则表达式对象。该对象拥有一系列方法用于正则表达式匹配和替换。 

re 模块也提供了与这些方法功能完全一致的函数，这些函数使用一个模式字符串做为它们的第一个参数。

本章节主要介绍 Python 中常用的正则表达式处理函数，如果你对正则表达式不了解，可以查看我们的 [正则表达式 - 教程](https://www.runoob.com/regexp/regexp-tutorial.html)。



## 1 正则表达式模式

模式字符串使用特殊的语法来表示一个正则表达式。

字母和数字表示他们自身。一个正则表达式模式中的字母和数字匹配同样的字符串。

多数字母和数字前加一个反斜杠时会拥有不同的含义。

标点符号只有被转义时才匹配自身，否则它们表示特殊的含义。

反斜杠本身需要使用反斜杠转义。

由于正则表达式通常都包含反斜杠，所以你最好使用原始字符串来表示它们。模式元素(如 r'\t'，等价于 \\t )匹配相应的特殊字符。

下表列出了正则表达式模式语法中的特殊元素。如果你使用模式的同时提供了可选的标志参数，某些模式元素的含义会改变。

| 模式         | 描述                                                         |
| ------------ | ------------------------------------------------------------ |
| .            | 匹配任意字符，除了换行符，当re.DOTALL标记被指定时，则可以匹配包括换行符的任意字符 |
| \d           | 匹配任意数字，等价于 [0-9]                                   |
| \D           | 匹配任意非数字                                               |
| \w           | 匹配数字字母下划线                                           |
| \W           | 匹配非数字字母下划线                                         |
| \s           | 匹配任意空白字符，等价于 [\t\n\r\f]。                        |
| \S           | 匹配任意非空字符                                             |
| ^            | 匹配字符串的开头                                             |
| $            | 匹配字符串的末尾                                             |
| \A           | 匹配字符串开始                                               |
| \z           | 匹配字符串结束                                               |
| \Z           | 匹配字符串结束，如果是存在换行，只匹配到换行前的结束字符串   |
| \G           | 匹配最后匹配完成的位置。                                     |
| \b           | 匹配一个单词边界，也就是指单词和空格间的位置。例如， 'er\b' 可以匹配"never" 中的 'er'，但不能匹配 "verb" 中的 'er' |
| \B           | 匹配非单词边界。'er\B' 能匹配 "verb" 中的 'er'，但不能匹配 "never" 中的 'er' |
| \n, \t, 等。 | 匹配一个换行符。匹配一个制表符, 等                           |
| \1...\9      | 匹配第n个分组的内容。 分组就是 () 中的内容                   |
| \10          | 匹配第n个分组的内容，如果它经匹配。否则指的是八进制字符码的表达式。 分组就是 () 中的内容 |

----
| 范围   | 描述                                                         |
| ------ | ------------------------------------------------------------ |
| [...]  | 用来表示一组字符,单独列出：[amk] 匹配 'a'，'m'或'k'          |
| [^...] | 不在[]中的字符：[^abc] 匹配除了a,b,c之外的字符               |
| ?      | 匹配0个或1个由前面的正则表达式定义的片段，非贪婪方式         |
| *      | 匹配0个或多个的表达式                                        |
| +      | 匹配1个或多个的表达式                                        |
| {n}    | 匹配n个前面表达式。例如，"o{2}"不能匹配"Bob"中的"o"，但是能匹配"food"中的两个o |
| {n,}   | 精确匹配n个前面表达式。例如，"o{2,}"不能匹配"Bob"中的"o"，但能匹配"foooood"中的所有o。"o{1,}"等价于"o+"。"o{0,}"则等价于"o*" |
| {n, m} | 匹配 n 到 m 次由前面的正则表达式定义的片段，贪婪方式         |


----
| 模式         | 描述                                                         |
| ------------ | ------------------------------------------------------------ |
| a\|b   | 匹配a或b                                                     |
| (re)         | 匹配括号内的表达式，也表示一个组                             |
| (?imx)       | 正则表达式包含三种可选标志：i, m, 或 x 。只影响括号中的区域  |
| (?-imx)      | 正则表达式关闭 i, m, 或 x 可选标志。只影响括号中的区域       |
| (?: re)      | 类似 (...), 但是不表示一个组                                 |
| (?imx: re)   | 在括号中使用i, m, 或 x 可选标志                              |
| (?-imx: re)  | 在括号中不使用i, m, 或 x 可选标志                            |
| (?#...)      | 注释.                                                        |
| (?= re)      | 前向肯定界定符。如果所含正则表达式，以 ... 表示，在当前位置成功匹配时成功，否则失败。但一旦所含表达式已经尝试，匹配引擎根本没有提高；模式的剩余部分还要尝试界定符的右边 |
| (?! re)      | 前向否定界定符。与肯定界定符相反；当所含表达式不能在字符串当前位置匹配时成功 |
| (?> re)      | 匹配的独立模式，省去回溯                                     |


------

## 2 正则表达式实例

### 字符匹配

| 实例   | 描述           |
| ------ | -------------- |
| python | 匹配 "python". |

### 字符类

| 实例        | 描述                              |
| ----------- | --------------------------------- |
| [Pp]ython   | 匹配 "Python" 或 "python"         |
| rub[ye]     | 匹配 "ruby" 或 "rube"             |
| [aeiou]     | 匹配中括号内的任意一个字母        |
| [0-9]       | 匹配任何数字。类似于 [0123456789] |
| [a-z]       | 匹配任何小写字母                  |
| [A-Z]       | 匹配任何大写字母                  |
| [a-zA-Z0-9] | 匹配任何字母及数字                |
| [^aeiou]    | 除了aeiou字母以外的所有字符       |
| [^0-9]      | 匹配除了数字外的字符              |

### 特殊字符类

| 实例 | 描述                                                         |
| ---- | ------------------------------------------------------------ |
| .    | 匹配除 "\n" 之外的任何单个字符。要匹配包括 '\n' 在内的任何字符，请使用象 '[.\n]' 的模式。 |
| \d   | 匹配一个数字字符。等价于 [0-9]。                             |
| \D   | 匹配一个非数字字符。等价于 [^0-9]。                          |
| \s   | 匹配任何空白字符，包括空格、制表符、换页符等等。等价于 [ \f\n\r\t\v]。 |
| \S   | 匹配任何非空白字符。等价于 [^ \f\n\r\t\v]。                  |
| \w   | 匹配包括下划线的任何单词字符。等价于'[A-Za-z0-9_]'。         |
| \W   | 匹配任何非单词字符。等价于 '[^A-Za-z0-9_]'。                 |

----

## 3 正则表达式修饰符 - flag

正则表达式可以包含一些可选标志修饰符来控制匹配的模式。修饰符被指定为一个可选的标志。多个标志可以通过按位 OR(|) 它们来指定。如 re.I | re.M 被设置成 I 和 M 标志：

| 修饰符    | 描述                                                         |
| --------- | ------------------------------------------------------------ |
| re.I      | 使匹配对大小写不敏感                                         |
| re.L      | 做本地化识别（locale-aware）匹配                             |
| re.M      | 多行匹配，影响 ^ 和 $                                        |
| re.S      | 使 . 匹配包括换行在内的所有字符                              |
| re.U      | 根据Unicode字符集解析字符。这个标志影响 \w, \W, \b, \B.      |
| re.X      | 该标志通过给予你更灵活的格式以便你将正则表达式写得更易于理解。 |
| re.DOTALL | . 匹配任意字符，除了换行符，当re.DOTALL标记被指定时，则可以匹配包括换行符的任意字符。 |



------

## 4 re.match() 开始位置匹配

re.match 尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none。

**函数语法**：

```python
re.match(pattern, string, flags=0)
```

> 函数参数说明：

- pattern: 匹配的正则表达式
- string: 要匹配的字符串。
- flags: 标志位，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等等。

> 返回:

- 匹配成功re.match方法返回一个匹配的对象，否则返回None。

我们可以使用group(num) 或  groups() 匹配对象函数来获取匹配表达式。

| 匹配对象方法 | 描述                                                         |
| ------------ | ------------------------------------------------------------ |
| group(num=0) | 匹配的整个表达式的字符串，group() 可以一次输入多个组号，在这种情况下它将返回一个包含那些组所对应值的元组。 |
| groups()     | 返回一个包含所有小组字符串的元组，从 1 到 所含的小组号。     |

### match() 实例

```python
import re

# re.match 尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none。

# 找到使用 .span() 返回位置
print(re.match('www', 'www.baidu.com'))   
# <_sre.SRE_Match object; span=(0, 3), match='www'>

print(re.match('www', 'www.baidu.com').span())
# (0, 3)

print(re.match('com', 'www.baidu.com'))          
# None
```

### group() 实例

```python
# group(num=0) 匹配的整个表达式的字符串，group() 可以一次输入多个组号，在这种情况下它将返回一个包含那些组所对应值的元组。
# groups()     返回一个包含所有小组字符串的元组，从 1 到 所含的小组号。

line = "Cats are smarter than dogs"
# 开始的r是为了让正则更明显
# .* 表示任意匹配除换行符（\n、\r）之外的任何单个或多个字符
# (.*?) 表示"非贪婪"模式，只保存第一个匹配到的子串
# re.M: 多行匹配，影响 ^ 和 $   
# re.I: 使匹配对大小写不敏感
matchObj = re.match( r'(.*) are (.*?) .*', line, re.M|re.I)
 
if matchObj:
   print("matchObj.group() : ", matchObj.group())      # 返回全部匹配
   print("matchObj.group(1) : ", matchObj.group(1))    # 返回上面第一个 () 的匹配
   print("matchObj.group(2) : ", matchObj.group(2))    # 返回上面第二个 () 的匹配
else:
   print("No match!!")

# matchObj.group() :  Cats are smarter than dogs    
# matchObj.group(1) :  Cats
# matchObj.group(2) :  smarter

```

### 结果 group() span() start() end() 

在上面，当匹配成功时返回一个 Match 对象，其中：

- `group([group1, …])` 方法用于获得一个或多个分组匹配的字符串，当要获得整个匹配的子串时，可直接使用 `group()` 或 `group(0)`；
- `start([group])` 方法用于获取分组匹配的子串在整个字符串中的起始位置（子串第一个字符的索引），参数默认值为 0；
- `end([group])` 方法用于获取分组匹配的子串在整个字符串中的结束位置（子串最后一个字符的索引+1），参数默认值为 0；
- `span([group])` 方法返回 `(start(group), end(group))`。

```python
# group()/group(0) 返回字符串位置索引
print(re.match('www', 'www.baidu.com').group()) # www

# span() 返回字符串位置索引
print(re.match('www', 'www.baidu.com').span())  # (0, 3)

# start() 返回字符串开始范围
print(re.match('www', 'www.baidu.com').start()) # 0

# end() 返回字符串结束位置
print(re.match('www', 'www.baidu.com').end())   # 3
```

------

## 5 search() 搜索第一个

re.search 扫描整个字符串并返回第一个成功的匹配。

函数语法：

```python
re.search(pattern, string, flags=0)
```

函数参数说明：

> 函数参数说明：

- pattern: 匹配的正则表达式
- string: 要匹配的字符串。
- flags: 标志位，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等等。

> 返回:

- 匹配成功re.search方法返回一个匹配的对象，否则返回None。

**我们可以使用group(num) 或  groups() 匹配对象函数来获取匹配表达式。**

| 匹配对象方法 | 描述                                                         |
| ------------ | ------------------------------------------------------------ |
| group(num=0) | 匹配的整个表达式的字符串，group() 可以一次输入多个组号，在这种情况下它将返回一个包含那些组所对应值的元组。 |
| groups()     | 返回一个包含所有小组字符串的元组，从 1 到 所含的小组号。     |

### search() 实例

```python
#!/usr/bin/python3
 
import re
 
print(re.search('www', 'www.runoob.com').span())  # 在起始位置匹配
print(re.search('com', 'www.runoob.com').span())  # 不在起始位置匹配
# (0, 3)
# (11, 14)
```

### group() 实例 

```python
#!/usr/bin/python3
 
import re

line = "Cats are smarter than dogs"
# 开始的r是为了让正则更明显
# .* 表示任意匹配除换行符（\n、\r）之外的任何单个或多个字符
# (.*?) 表示"非贪婪"模式，只保存第一个匹配到的子串
# re.M: 多行匹配，影响 ^ 和 $   
# re.I: 使匹配对大小写不敏感
searchObj = re.search( r'(.*) are (.*?) .*', line, re.M|re.I)
 
if searchObj:
   print("searchObj.group() : ", searchObj.group())
   print("searchObj.group(1) : ", searchObj.group(1))
   print("searchObj.group(2) : ", searchObj.group(2))
else:
   print("Nothing found!!")
# searchObj.group() :  Cats are smarter than dogs   
# searchObj.group(1) :  Cats
# searchObj.group(2) :  smarter
```

------

## 6 re.match与re.search的区别

re.match 只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回 None，而 re.search 匹配整个字符串，直到找到一个匹配。

### 实例 

```python
#!/usr/bin/python3
 
import re
 
line = "Cats are smarter than dogs"
 
# re.M: 多行匹配，影响 ^ 和 $   
# re.I: 使匹配对大小写不敏感
matchObj = re.match( r'dogs', line, re.M|re.I)
if matchObj:
   print("match --> matchObj.group() : ", matchObj.group())
else:
   print("No match!!")
# No match!!

matchObj = re.search( r'dogs', line, re.M|re.I)
if matchObj:
   print("search --> matchObj.group() : ", matchObj.group())
else:
   print("No match!!")
# search --> matchObj.group() :  dogs
```

----

## 7 compile() 编译正则表达式 多个方法可用 可以选择开始结束位置

compile 函数用于编译正则表达式，生成一个正则表达式（ Pattern ）对象，供 match(), search(),findall() 等多个函数使用

语法格式为：

```python
re.compile(pattern[, flags])
```

参数：

- pattern : 一个字符串形式的正则表达式
- flags 可选，表示匹配模式，比如忽略大小写，多行模式等，具体参数为：
- re.I 忽略大小写

    - re.L 表示特殊字符集 \w, \W, \b, \B, \s, \S 依赖于当前环境
    - re.M 多行模式
    - re.S 即为' . '并且包括换行符在内的任意字符（' . '不包括换行符）
    - re.U 表示特殊字符集 \w, \W, \b, \B, \d, \D, \s, \S 依赖于 Unicode 字符属性数据库
    - re.X 为了增加可读性，忽略空格和' # '后面的注释

返回RegexObject 对象

### match() 实例

```python
import re

# 用于匹配至少一个数字
pattern = re.compile(r'\d+')                    
m = pattern.match('one12twothree34four')        # 查找头部，没有匹配
print(m)    # None


m = pattern.match('one12twothree34four', 2, 10) # 从第2的位置开始匹配，没有匹配
print(m)    # None

m = pattern.match('one12twothree34four', 3, 10) # 从第3的位置开始匹配，正好匹配
print(m)                                        # 返回一个 Match 对象


print(m.group(0))   # 第一个匹配到的内容
# 12
print(m.start(0))   # 开始位置
# 3
print(m.end(0))     # 结束位置
# 5
print(m.span(0))    # 匹配字符串范围
# (3, 5)
```

在上面，当匹配成功时返回一个 Match 对象，其中：

- `group([group1, …])` 方法用于获得一个或多个分组匹配的字符串，当要获得整个匹配的子串时，可直接使用 `group()` 或 `group(0)`；
- `start([group])` 方法用于获取分组匹配的子串在整个字符串中的起始位置（子串第一个字符的索引），参数默认值为 0；
- `end([group])` 方法用于获取分组匹配的子串在整个字符串中的结束位置（子串最后一个字符的索引+1），参数默认值为 0；
- `span([group])` 方法返回 `(start(group), end(group))`。

再看看一个例子：

### group() span() start() end() 实例

```python
import re

pattern = re.compile(r'([a-z]+) ([a-z]+)', re.I)   # re.I 表示忽略大小写
m = pattern.match('Hello World Wide Web')
print(m)            # 匹配成功，返回一个 Match 对象
# <_sre.SRE_Match object; span=(0, 11), match='Hello World'>

print(m.groups())          # 等价于 (m.group(1), m.group(2), ...)
# ('Hello', 'World')

print(m.group(0))          # 返回匹配成功的整个子串
# Hello World
print(m.span(0))           # 返回匹配成功的整个子串的索引
# (0, 11)
print(m.start(0))
# 0
print(m.end(0))
# 11

print(m.group(1))          # 返回第一个分组匹配成功的子串
# Hello
print(m.span(1))           # 返回第一个分组匹配成功的子串的索引
# (0, 5)

print(m.group(2))          # 返回第二个分组匹配成功的子串
# World
print(m.span(2))           # 返回第二个分组匹配成功的子串索引
# (6, 11)

m.group(3)          # 不存在第三个分组
# Traceback (most recent call last):
#   File "d:/Python/Pycharm/01/day13 re正则表达式/2 compile.py", line 69, in <module>
#     m.group(3)          # 不存在第三个分组
# IndexError: no such group
```

### search() 实例

```python
pattern = re.compile(r'\d+')
s = pattern.search('a9a0k10kae')
print(s)
# <_sre.SRE_Match object; span=(1, 2), match='9'>
print(s.group())
# 9
print(s.span())     # (1, 2)
print(s.start())    # 1
print(s.end())      # 2
```

### findall() finditer() 实例

```python
pattern = re.compile(r'\d+')
f = pattern.findall('a9a0k10kae')
print(f)    # ['9', '0', '10']


pattern = re.compile(r'\d+')
f = pattern.finditer('a9a0k10kae')
print(next(f).group())  	# 9
```

### split() 实例

```python
# 可以使用compile
pattern = re.compile('\W+')
print(pattern.split('aa, bb, cc'))      # ['aa', 'bb', 'cc']
```

### sub() 实例

```python
phone = "2004-959-559 # 这是一个电话号码"

# 使用compile
# 移除非数字的内容
pattern = re.compile(r'\D')
#                 替换内容
print(pattern.sub('', phone))   # 2004959559
```

----

## 8 findall() 所有子串返回列表

在字符串中找到正则表达式所匹配的所有子串，并返回一个列表，如果没有找到匹配的，则返回空列表。

**注意：** match 和 search  是匹配一次 findall 匹配所有。

语法格式为：

```python
re.findall(pattern, string, flags=0)
或
pattern.findall(string[, pos[, endpos]])
```

> 参数：

- pattern 匹配模式。
- string 待匹配的字符串。
- flags: 标志位，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等等。
- pos 可选参数，指定字符串的起始位置，默认为 0。
- endpos 可选参数，指定字符串的结束位置，默认为字符串的长度。

> 返回列表

### findall() 实例

查找字符串中的所有数字：

```python
import re
 
print(re.findall(r'\d+','runoob 123 google 456'))               # ['123', '456']

pattern = re.compile(r'\d+')   # 查找数字
print(pattern.findall('runoob 123 google 456'))                 # ['123', '456']
print(pattern.findall('run88oob123google456', pos=0, endpos=10))# ['88', '12']
```

----

## 9 finditer 所有子串返回迭代器

和 findall 类似，在字符串中找到正则表达式所匹配的所有子串，并把它们作为一个迭代器返回。

```python
re.finditer(pattern, string, flags=0)
或
pattern.finditer(string[, pos[, endpos]])
```

> 参数：

 - pattern 匹配模式。
 - string 待匹配的字符串。
 - flags: 标志位，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等等。
 - pos 可选参数，指定字符串的起始位置，默认为 0。
 - endpos 可选参数，指定字符串的结束位置，默认为字符串的长度。

> 返回迭代器

### finditer 实例

```python
import re
 
iter = re.finditer(r'\d+','runoob 123 google 456')       
for i in iter:
    print(i.group())
print('-' * 50)
# 123
# 456

pattern = re.compile(r'\d+')   # 查找数字
iter = pattern.finditer('runoob 123 google 456')   
for i in iter:
    print(i.group())
print('-' * 50)
# 123
# 456

iter = pattern.finditer('run88oob123google456', pos=0, endpos=10)
for i in iter:
    print(i.group())
# 88
# 12
```

----

## 10 split() 分裂返回列表

split 方法按照能够匹配的子串将字符串分割后返回列表，它的使用形式如下：

```python
re.split(pattern, string[, maxsplit=0, flags=0])
```

> 参数：

- pattern: 匹配的正则表达式
- string: 要匹配的字符串。
- maxsplit: 分割次数，maxsplit=1 分割一次，默认为 0，不限制次数。
- flags: 标志位，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等等。参见：[正则表达式修饰符 - 可选标志](https://www.runoob.com/python3/python3-reg-expressions.html#flags)

> 返回列表

### split() 实例

```python
import re

# \W 是除了数字字母下划线
print(re.split('\W+', 'aa, bb, cc.'))       # ['runoob', 'runoob', 'runoob', '']

print(re.split('(\W+)', ' aa, bb, cc.'))    # ['', ' ', 'runoob', ', ', 'runoob', ', ', 'runoob', '.', '']

# 只分裂两次
print(re.split('\W+', ' aa, bb, cc.', 1))   # ['', 'aa, bb, cc.']


# 对于一个找不到匹配的字符串而言，split 不会对其作出分割,但是会警告
print(re.split('a*', 'hello world'))   
# D:\Anaconda3\envs\ai\lib\re.py:212: FutureWarning: split() requires a non-empty pattern match.
#   return _compile(pattern, flags).split(string, maxsplit)
# ['hello world']
```

### compile split() 实例

```python
# 可以使用compile
pattern = re.compile('\W+')
print(pattern.split('aa, bb, cc'))      # ['aa', 'bb', 'cc']
```

----

## 11 sub() 检索和替换

Python 的re模块提供了re.sub用于替换字符串中的匹配项。

语法：

```python
re.sub(pattern, repl, string, count=0, flags=0)
```

> 参数：

- pattern : 正则中的模式字符串。
- repl : 替换的字符串，也可为一个函数。
- string : 要被查找替换的原始字符串。
- count : 模式匹配后替换的最大次数，默认 0 表示替换所有的匹配。
- flags : 编译时用的匹配模式，数字形式。

 **前三个为必选参数，后两个为可选参数。**

> 返回新的字符串

### sub() 实例 

```python
#!/usr/bin/python3
import re
 
phone = "2004-959-559 # 这是一个电话号码"
 
# 删除注释
num = re.sub(r'#.*$', "", phone)
print ("电话号码 : ", num)
# 电话号码 :  2004-959-559 

# 移除非数字的内容
num = re.sub(r'\D', "", phone)
print ("电话号码 : ", num)
# 电话号码 :  2004-959-559 
```

### repl 参数可以是一个函数

以下实例中将字符串中的匹配的数字乘于 2：

#### repl闭包 实例 

```python
#!/usr/bin/python
 
import re
 
# 将匹配的数字乘于 2
def double(matched):
    value = int(matched.group('value'))
    return str(value * 2)
 
s = 'A23G4HFD567'
print(re.sub(r'(?P<value>\d+)', double, s))
# A46G8HFD1134 数字变为2倍

print(re.search(r'(?P<value>\d+)', s).span())
# (1, 3) 找到第一个位置
```

### compile sub() 实例

```python
phone = "2004-959-559 # 这是一个电话号码"

# 使用compile
# 移除非数字的内容
pattern = re.compile(r'\D')
#                 替换内容
print(pattern.sub('', phone))   # 2004959559
```



## 12 正则表达式对象

### re.RegexObject

re.compile() 返回 RegexObject 对象。

### re.MatchObject

- group() 返回被 RE 匹配的字符串。

- start() 返回匹配开始的位置
- end() 返回匹配结束的位置
- span() 返回一个元组包含匹配 (开始,结束) 的位置
----

## 13 英文字母分词

```python
import re


def tokenize(text):
    '''
    英文句子分成单个的单词,去除标点符号
    '''

    # fileters = '!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~\t\n'
    fileters = ['!', '"', '#', '$', '%', '&', '\(', '\)', '\*', '\+', ',', '-', '\.', '/', ':', ';', '<', '=', '>',
                '\?', '@', '\[', '\\', '\]', '^', '_', '`', '\{', '\|', '\}', '~', '\t', '\n', '\x97', '\x96', '”', '“', ]
    # 替换 <??> 为 ""
    text = re.sub("<.*?>", " ", text, flags=re.S)   # re.S: 使 . 匹配包括换行在内的所有字符
    # 替换出现的字符为 ""
    text = re.sub("|".join(fileters), " ", text, flags=re.S)    # re.S: 使 . 匹配包括换行在内的所有字符
    # 分隔文本并去除空格
    return [i.strip() for i in text.split()]


if __name__ == '__main__':
    res = tokenize('hello world, my name is Yuki!!!')
    print(res)
    # ['hello', 'world', 'my', 'name', 'is', 'Yuki']
```