#!/usr/bin/python3
my_list = [5, 4, 3, 2, 1]
even_or_odd = []

for i in my_list:
    if i % 2 ==0:
            even_or_odd.append(True)
    else:
            even_or_odd.append(False)            
even_or_odd = tuple(even_or_odd)
print(my_list)
print(even_or_odd)
