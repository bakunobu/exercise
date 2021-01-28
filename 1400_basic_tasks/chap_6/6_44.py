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


def even_diff(n:int) -> bool:
    x = min_max_dif(n)
    return(x % 2 == 0)