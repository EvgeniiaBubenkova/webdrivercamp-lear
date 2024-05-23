def tuple_return(arg):
    if len(arg) == 0:
        first_element = None
    else:
        first_element = arg[0]
    return len(arg), first_element

