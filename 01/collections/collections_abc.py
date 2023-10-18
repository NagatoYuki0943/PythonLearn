import collections.abc

l = [1, 2, 3]
t = (1, 2)
d = {1: "a", 2: "b"}

print(isinstance(l, collections.abc.Iterable))  # True
print(isinstance(t, collections.abc.Iterable))  # True
print(isinstance(d, collections.abc.Iterable))  # True
