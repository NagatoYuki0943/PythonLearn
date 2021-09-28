'''
从下到上依次装饰
先执行 makeBold, 返回值再执行 makehItalic

@ makehItalic
@ makeBold
def hello():
    pass

'''


def makeBold(func):
    """文字加粗"""
    def func_in():
        print("文字加粗")
        # 在hello前后加标签
        return "<b>" + func() + "</b>"

    return func_in


def makehItalic(func):
    """文字倾斜"""
    def func_in():
        print("文字倾斜")
        # 在hello前后加标签
        return "<i>" + func() + "</i>"

    return func_in


# 从下到上依次装饰
# 先执行 makeBold, 返回值再执行 makehItalic

@ makehItalic
@ makeBold
def hello():
    return "hello-1"



print(hello())
# 文字倾斜
# 文字加粗
# <i><b>hello-1</b></i>

# "文字倾斜"出现在"文字加粗前面", 是因为先调用了 makeBold,返回的是 func_in 函数,这个函数没有执行,
# 而是传递给了 makehItalic函数,makehItalic中的func就是传递过来的 "func_in",然后返回它自己的"func_in",
# 执行这个func_in的时候,先输出"文字倾斜",再调用func, 就是makeBold中的 func_in, 所以会打印 "文字加粗",最后调用hello()函数