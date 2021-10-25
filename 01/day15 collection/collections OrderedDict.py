'''
Python字典中的键的顺序是任意的:它们不受添加的顺序的控制。
`collections.OrderedDict `类提供了保留他们添加顺序的字典对象。
如果在已经存在的key上添加新的值，将会保留原来的key的位置，然后覆盖value值。
'''

from collections import OrderedDict


o = OrderedDict()

o['key2'] = 'value2'
o['key1'] = 'value1'
o['key3'] = 'value3'
print(o)
# OrderedDict([('key2', 'value2'), ('key1', 'value1'), ('key3', 'value3')])

o['key1'] = 'value4'
print(o)
# OrderedDict([('key2', 'value2'), ('key1', 'value4'), ('key3', 'value3')])

o.update({"keyx": "xxxxx"})
print(o)
# OrderedDict([('key2', 'value2'), ('key1', 'value4'), ('key3', 'value3'), ('keyx', 'xxxxx')])