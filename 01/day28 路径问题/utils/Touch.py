'''
无论是在外面直接建立对象,还是在内层建立对象再返回,都是在外面创建txt
'''

class Touch(object):
    def __init__(self, path) -> None:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(str(111))

        with open(path, 'r', encoding='utf-8') as f:
            print(f.read())