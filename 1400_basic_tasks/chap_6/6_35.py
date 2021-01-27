# a
def count_three(n:int) -> int:
    counter = 0
    while n:
        num = n % 10
        if num == 3:
            counter += 1
        n //= 10
    return(counter)


# b
def count_last_digit(n:int) -> int:
    ld = n % 10
    counter = 0
    while n:
        num = n % 10
        if num == ld:
            counter += 1
        n //= 10
    return(counter)


# c
def count_even(n:int) -> int:
    counter = 0
    while n:
        num = n % 10
        if num % 2 == 0:
            counter += 1
        n //= 10
    return(counter)


# d
def count_sum_gt_five(n:int) -> int:
    total = 0
    while n:
        num = n % 10
        if num > 5:
            total += num
        n //= 10
    return(total)


# e
def count_zero_five(n:int) -> int:
    counter = 0
    while n:
        num = n % 10
        if num in (0, 5):
            counter += num
        n //= 10
    return(counter)