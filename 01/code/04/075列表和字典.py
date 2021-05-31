'''
在字典中可以包含列表，列表中能包含字典吗？
可以的， 列表 元组可以存放任意类型的数据，同样，字典中的 valu也可以是任意的类型，字典也可以作为字典的 value 值。
'''

dict = {'name': 'Tom', 'age': 18, 'hobby': ['pantyhose', 'sticks', 'stocking']}

list = [
    {'name': 'Tom', 'age': 18, 'hobby': ['pantyhose', 'sticks', 'stocking']},
    {'name': 'Jerry', 'age': 14, 'hobby': ['kuwa', 'siwa']},
    {'name': 'Uncle', 'age': 60, 'hobby': ['leotard', 'tights']}
]

for i in list:
    print(i['name'], i['age'])
    for h in i['hobby']:
        print(h, end=" ")
    print()

# Tom 18
# pantyhose sticks stocking
# Jerry 14
# kuwa siwa
# Uncle 60
# leotard tights