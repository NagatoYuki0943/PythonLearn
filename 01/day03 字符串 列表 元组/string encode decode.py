str1 = "Sebastian\n你好"

print(str1.encode())  # b'Sebastian\n\xe4\xbd\xa0\xe5\xa5\xbd'
code = str1.encode("utf-8")
print(code)  # b'Sebastian\n\xe4\xbd\xa0\xe5\xa5\xbd'
print(code.decode("utf-8"))
# Sebastian
# 你好
# repr 返回原始数据
print(repr(code.decode("utf-8")))  # 'Sebastian\n你好'
