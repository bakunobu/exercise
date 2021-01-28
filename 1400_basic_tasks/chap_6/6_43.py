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


def is_div_a(n:int, a:int) -> bool:
    x = min_max_sum(n)
    return(x % a == 0)

