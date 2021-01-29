# a
def num_sum(n: int, k:int) -> bool:
    total = 0
    while n:
        num = n % 10
        total += num
        n //= 10
    return(total > k and not total % 2)


# b
def find_length_alt(n:int, b:int) -> bool:
    i = 0
    while n:
        i += 1
        n //= 10
    return(not i % 2 and n < b)


# c
def first_last_dig(n:int, x:int, y:int) -> bool:
    first_dig = 0
    last_dig = n % 10
    while n:
        first_dig = n % 10
        n //= 10
    return(first_dig == x and last_dig == y)


# d
def num_prod(n:int, a:int, b:int) -> bool:
    prod = 1
    while n:
        num = n % 10
        prod *= num
        n //= 10
    return(prod < a and not n % b)


# e
def num_sum(x:int, n: int, m:int) -> bool:
    total = 0
    while x:
        num = x % 10
        total += num
        x //= 10
    return(total > m and not total % n)

