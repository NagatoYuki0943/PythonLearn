'''
json.dumps 	将 Python 对象编码成 JSON 字符串
json.loads	将已编码的 JSON 字符串解码为 Python 对象
'''

from json import dumps,loads


json_name = "test.json"
dict1 = {"0":"a", "1":"b", "2":"c"}


# 写入文件
with open(json_name, mode='w', encoding='utf-8') as f:
    str1 = dumps(dict1)
    print(type(dict1))  # <class 'dict'>
    print(type(str1))   # <class 'str'>
    f.write(str1)


with open(json_name, mode='r', encoding='utf-8') as f:
    str2 = f.read()
    dict2 = loads(str2)

    print(type(dict2))  # <class 'dict'>
    print(type(str2))   # <class 'str'>

    print(dict2['0'])   # a