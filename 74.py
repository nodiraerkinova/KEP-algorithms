def even_index_or_value(numbers):
    r = []
    for num in range(len(numbers)):
        if num % 2 == 0 or numbers[num] % 2 == 0:
            r.append(numbers[num])
    return r 