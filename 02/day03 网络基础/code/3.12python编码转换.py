'''
编码
    符串.encode()      默认UTF-8字符串

* 解码
    二进制.decode()    默认UTF-8字符集

* 解码失败的处理
    decode(encoding="字符集", errors="错误处理方式")
    错误处理方式有两种：ignore 忽略， strict 严格

'''
string = '你好'.encode(encoding='gbk')
print(string)   # b'\xc4\xe3\xba\xc3'

# errors设置为了ignore,转码失败不管
string = string.decode(encoding='utf-8', errors='ignore')
print(string)   # 你好  写gbk才输出, errors设置为了ignore,转码失败不管