#!/usr/bin/python3
def max_value(d):
    def max_num(dict_):
        if not dict_:
            return None
        max_num = 0
        for i in dict_.values():
            if i > max_num:
                max_num = i
        return max_num

    if __name__=="__main__":
        dict_ = {'Apple': 13, 'Pear': 1, 'Plum': 20, 'Grape': 10}
        max_key = max_value(dict_)
        print(f"Max number - {max_key}")

        max_key = max_value(None)
        print(f"Max number - {max_key}")

max_value(None)
 
