# a
def num_digits(n:int) -> int:
    num_sum = 0
    while n:
        num_sum += n % 10
        n //= 10
    return(num_sum)


# b
def quant_digits(n:int) -> int:
    i = 0
    while n:
        i += 1
        n //= 10
    return(i)

# c
def prod_digits(n:int) -> int:
    num_prod = 1
    while n:
        num_prod *= n % 10
        n //= 10
    return(num_prod)

# d
def mean_dig(n:int) -> float:
    s = num_digits(n)
    d = quant_digits(n)
    return(s / d)


# e
def sqrd_sum_digits(n:int) -> int:
    num_sum = 0
    while n:
        num_sum += (n % 10) ** 2
        n //= 10
    return(num_sum)


# f
def cubed_sum_digits(n:int) -> int:
    num_sum = 0
    while n:
        num_sum += (n % 10) ** 3
        n //= 10
    return(num_sum)


# g
def first_n_last_sum(n:int) -> int:
    i = n % 10
    while n > 10:
        n //= 10
    return(i + n)


