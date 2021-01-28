# a
def min_max_digit(n:int) -> tuple:
    min_dig = 9
    max_dig = 0
    while n:
        num =  n % 10
        if num < min_dig:
            min_dig = num
        if num > max_dig:
            max_dig = num
        n //= 10
    return(min_dig, max_dig)


# b
def min_max_dif(n:int) -> int:
    min_dig = 9
    max_dig = 0
    while n:
        num =  n % 10
        if num < min_dig:
            min_dig = num
        if num > max_dig:
            max_dig = num
        n //= 10
    return(max_dig-min_dig)


# c
def min_max_sum(n:int) -> int:
    min_dig = 9
    max_dig = 0
    while n:
        num =  n % 10
        if num < min_dig:
            min_dig = num
        if num > max_dig:
            max_dig = num
        n //= 10
    return(min_dig + max_dig)