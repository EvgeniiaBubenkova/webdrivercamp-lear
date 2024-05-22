#!/usr/bin/python3
def only_unique(list_=[]):
    x = set()
    total = 0
    for i in list_:
        if i not in x:
            total += i
            x.add(i)
    return total

if __name__=="__main__":
    list_ = [0, 1, 6, 3, 6, 4, 0, 2, 5, 4, 4]
    result = only_unique(list_)
    print(f"Sum of unique: {result}")

