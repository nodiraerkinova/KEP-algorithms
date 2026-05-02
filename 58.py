def filter_list(lst, son):
    if son == 0:
        for num in lst:
            if num % 2 == 0:
                lst.remove(num)
        return lst
    else:
        for num in lst:
            if num % 2 != 0:
                lst.remove(num)
        return lst

print(filter_list([1, 2, 3, 4, 5], 0))

