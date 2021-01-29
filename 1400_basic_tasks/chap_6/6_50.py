# a
def num_sum(n: int, a:int) -> bool:
    total = 0
    while n:
        num = n % 10
        total += num
        n //= 10
    return(total < a)


# b
def num_prod(n:int, b:int) -> bool:
    prod = 1
    while n:
        num = n % 10
        prod *= num
        n //= 10
    return(prod > b)


# c
def find_length_alt(n:int, k:int) -> bool:
    i = 0
    while n:
        i += 1
        n //= 10
    return(i == k)


# d
def first_dig(n:int, m:int) -> bool:
    first_dig = 0
    while n:
        first_dig = n % 10
        n //= 10
    return(first_dig > m)

