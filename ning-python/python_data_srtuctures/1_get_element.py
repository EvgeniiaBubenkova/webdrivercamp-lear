#!/usr/bin/python3

list_ = [5, 4, 3, 2, 1]
index = 2

for i in range(len(list_)):
    if index < 0 or index >= len(list_):
        print('The element retrieved is None')
    elif i == index:
        print(f'The element retrieved is {list_[i]}')

