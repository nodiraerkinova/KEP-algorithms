# Algorithim
# 1. max_1 ni topish
# 2. sonlarni ichidan max_1 ni o'chirish
# 3. qolgan sonlar ichidan max ni top
def max_2(*args):
    max_1 = max(args)
    lst = list(args)   
    lst.remove(max_1)
    max_2 = max(lst) 
    return max_2
    