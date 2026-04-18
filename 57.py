def sum_digits(s):
    nums = 0
    for r in str(s):
        son = int(r)
        nums += son
    return nums     