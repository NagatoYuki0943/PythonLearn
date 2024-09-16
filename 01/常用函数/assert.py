"""
Python assert（断言）用于判断一个表达式，在表达式条件为 false 的时候触发异常。

断言可以在条件不满足程序运行的情况下直接返回错误，而不必等待程序运行后出现崩溃的情况

语法格式如下：
    assert expression

等价于：
    if not expression:
        raise AssertionError

assert 后面也可以紧跟参数:
    assert expression [, arguments]

等价于：
    if not expression:
        raise AssertionError(arguments)
"""

import random

a = random.random()

if a < 0.5:
    assert "a小于5"
