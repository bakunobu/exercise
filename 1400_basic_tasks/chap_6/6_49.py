# a
def num_sum(n: int) -> bool:
    total = 0
    while n:
        num = n % 10
        total += num
        n //= 10
    return(total > 10)


# b
def num_prod(n:int) -> bool:
    prod = 1
    while n:
        num = n % 10
        prod *= num
        n //= 10
    return(prod < 50)


# c
def find_length(n:int) -> bool:
    i = 0
    while n:
        i += 1
        n //= 10
    return(i % 2 == 0)


# d
def find_length_alt(n:int) -> bool:
    i = 0
    while n:
        i += 1
        n //= 10
    return(i == 4)


# e
def first_dig(n:int) -> bool:
    first_dig = 0
    while n:
        first_dig = n % 10
        n //= 10
    return(first_dig <= 6)


# f
def first_last_dig(n:int) -> bool:
    first_dig = 0
    last_dig = n % 10
    while n:
        first_dig = n % 10
        n //= 10
    return(first_dig == last_dig)


# g
def first_last_dig_comp(n:int) -> str:
    first_dig = 0
    last_dig = n % 10
    while n:
        first_dig = n % 10
        n //= 10
    if first_dig > last_dig:
        return('First')
    else:
        return('Last')