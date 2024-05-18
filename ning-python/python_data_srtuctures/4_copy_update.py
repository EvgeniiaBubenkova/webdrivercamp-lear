#!/usr/bin/python3

list_ = [5, 4, 3, 2, 1]
index = 1
element_to_replace = 5
copy=list_[:]
if index >= 0 and index < len(list_):
    copy[index] = element_to_replace

print("Copy:", copy)
print("Original:", list_)

