# a
def min_max_indices(n:int) -> tuple:
    i = 0
    min_dig = 9
    max_dig = 0
    min_i = 0
    max_i = 0
    while n:
        num = n % 10
        if num > max_dig:
            max_dig = num
            max_i = i
        if num < min_dig:
            min_dig = num
            min_i = i
    return(min_i, max_i)


# b
def min_max_indices(n:int) -> tuple:
    i = 0
    min_dig = 9
    max_dig = 0
    min_i = 0
    max_i = 0
    while n:
        num = n % 10
        if num > max_dig:
            max_dig = num
            max_i = i
        if num < min_dig:
            min_dig = num
            min_i = i
    return(i - (min_i + 1),
           i - (max_i + 1))
    