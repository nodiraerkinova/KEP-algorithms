def argv_int(*args):
    c = 0
    
    for arg in args:
        if type(arg) == int:
            c += 1
    return c        
print (argv_int(2, 4, "a", 5.0, None) == 2)
print(argv_int() == 0)