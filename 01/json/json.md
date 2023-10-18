# json需要配合open

# json.dump(文件对象)

json.dumps 用于将 Python 对象编码成 JSON 字符串。

```python
json.dump(
    obj, 					# 表示是要序列化的对象
    fp,						# 文件描述符，将序列化的str保存到文件中。json模块总是生成str对象，而不是字节对象；因此，fp.write（）必须支持str输入。
    skipkeys=False, 		# 默认为False,如果skipkeys = True,（默认值：False），则将跳过不是基本类型（str，int，float，bool，None）的dict键，不会引发TypeError。
    ensure_ascii=True, 		# 默认值为True,能将所有传入的非ASCII字符转义输出。如果ensure_ascii为False，则这些字符将按原样输出。
    check_circular=True, 	# 默认值为True,如果check_circular为False，则将跳过对容器类型的循环引用检查，循环引用将导致OverflowError。
    allow_nan=True, 		# 默认值为True,如果allow_nan为False，则严格遵守JSON规范,序列化超出范围的浮点值（nan，inf，-inf）会引发ValueError。 如果allow_nan为True,则将使用它们的JavaScript等效项（NaN，Infinity，-Infinity）。
    indent=None, 			# 设置缩进格式，默认值为None,选择的是最紧凑的表示。如果indent是非负整数或字符串，那么JSON数组元素和对象成员将使用该缩进级别进行输入；indent为0,负数或“”仅插入换行符；indent使用正整数缩进多个空格；如果indent是一个字符串（例如“\t”），则该字符串用于缩进每个级别。
    separators=None, 		# 去除分隔符后面的空格，默认值为None,如果指定，则分隔符应为（item_separator，key_separator）元组。如果缩进为None，则默认为（’，’，’：’）;要获得最紧凑的JSON表示，可以指定（’，’，’:’）以消除空格。
    encoding="utf-8", 		# 编码
    default=None, 			# 默认值为None,如果指定，则default应该是为无法以其他方式序列化的对象调用的函数。它应返回对象的JSON可编码版本或引发TypeError。如果未指定，则引发TypeError。
    sort_keys=False, 		# 默认值为False,如果sort_keys为True，则字典的输出将按键值排序。
    **kw
)
```

----

# json.dumps(字符串) 常用

`dumps`函数不需要传文件描述符，其他的参数和`dump`函数的一样。

```python
json.dumps(obj, 
           *, 
           skipkeys=False, 
           ensure_ascii=True, 	
           check_circular=True, 
           allow_nan=True, 
           cls=None, 
           indent=None, 
           separators=None, 
           default=None, 
           sort_keys=False, 
           **kw
          )
```

## 实例

```python
#!/usr/bin/python
import json

data = [ { 'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5 } ]

data2 = json.dumps(data)
print(data2)
```

以上代码执行结果为：

```python
[{"a": 1, "c": 3, "b": 2, "e": 5, "d": 4}]
```

使用参数让 JSON 数据格式化输出：

## 实例

```python
#!/usr/bin/python
import json

data = [ { 'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5 } ]

data2 = json.dumps({'a': 'Runoob', 'b': 7}, sort_keys=True, indent=4, separators=(',', ': '))
print(data2)
```



以上代码执行结果为：

```python
{
    "a": "Runoob",
    "b": 7
}
```



## 写入中文 ensure_ascii=False



python 原始类型向 json 类型的转化对照表：

| Python           | JSON   |
| ---------------- | ------ |
| dict             | object |
| list, tuple      | array  |
| str, unicode     | string |
| int, long, float | number |
| True             | true   |
| False            | false  |
| None             | null   |

----

# json.load(文件对象)

json.loads 用于解码 JSON 数据。该函数返回 Python 字段的数据类型。

```python
json.load(fp, 					# 文件描述符，将fp（.read（）支持包含JSON文档的文本文件或二进制文件）反序列化为Python对象。
           object_hook, 		# 默认值为None,object_hook是一个可选函数，此功能可用于实现自定义解码器。指定一个函数，该函数负责把反序列化后的基本类型对象转换成自定义类型的对象。
           parse_float, 		# 默认值为None,如果指定了parse_float，用来对JSON float字符串进行解码,这可用于为JSON浮点数使用另一种数据类型或解析器。
           parse_int, 			# 默认值为None,如果指定了parse_int，用来对JSON int字符串进行解码,这可以用于为JSON整数使用另一种数据类型或解析器。
           parse_constant, 		# 默认值为None,如果指定了parse_constant,对-Infinity,Infinity,NaN字符串进行调用。如果遇到了无效的JSON符号，会引发异常。
           object_pairs_hook, 
           **kw
          )
```

----

# json.loads(字符串) 常用

`loads`也不需要文件描述符，其他参数的含义和`load`函数的一致。

```python
json.loads(s, 						# 将s（包含JSON文档的str，bytes或bytearray实例）反序列化为Python对象。 
           *, 				
           encoding=None, 			# 定一个编码的格式。 
           cls=None, 
           object_hook=None, 
           parse_float=None, 
           parse_int=None, 
           parse_constant=None, 
           object_pairs_hook=None, 
           **kw)
```

## 实例

```python
#!/usr/bin/python
import json

jsonData = '{"a":1,"b":2,"c":3,"d":4,"e":5}';

text = json.loads(jsonData)
print(text)
```

以上代码执行结果为：

```python
{u'a': 1, u'c': 3, u'b': 2, u'e': 5, u'd': 4}
```



## load loads 区别

```python
with open("C:\Ai\Garbage134\data\class2name.json", mode='r',encoding='utf-8') as f:
    class2name = json.load(f)			# 传入文件对象
    class2name = json.loads(f.read())	# 传入字符串
```





## json 类型转换到 python 的类型对照表：

| JSON          | Python    |
| ------------- | --------- |
| object        | dict      |
| array         | list      |
| string        | unicode   |
| number (int)  | int, long |
| number (real) | float     |
| true          | True      |
| false         | False     |
| null          | None      |