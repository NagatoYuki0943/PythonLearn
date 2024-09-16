'''
self:  self指的是类实例对象本身(注意：不是类本身)。
*args: 不定长参数
sep:   分隔符
end:   换行符

def print(self, *args, sep=' ', end='\n', file=None): # known special case of print
    """
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)

    Prints the values to a stream, or to sys.stdout by default.
    Optional keyword arguments:
    file:  a file-like object (stream); defaults to the current sys.stdout.
    sep:   string inserted between values, default a space.
    end:   string appended after the last value, default a newline.
    flush: whether to forcibly flush the stream.
    """
    pass
'''

print(1)  # 1
print(1, 2, sep="*")  # 1*2
print(1, 2, 3, sep="_*_")  # 1_*_2_*_3
print(1, 2, 3, 4, sep="hello")  # 1hello2hello3hello4
print(1, 2, 3, 4, 5, " ")  # 1 2 3 4 5
