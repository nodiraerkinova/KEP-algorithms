def max_2(*args):
    max_1 = max(args)
    lst = list(args)   
    lst.remove(max_1)
    max_2 = max(lst) 
    return max_2
    