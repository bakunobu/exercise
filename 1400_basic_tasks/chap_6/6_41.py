# a
def max_digit(n:int) -> int:
    md = 0
    while n:
        num = n % 10
        if md < num:
            md = num
        n //= 10
    return(md)


# b
def min_digit(n:int) -> int:
    md = 9
    while n:
        num = n % 10
        if md > num:
            md = num
        n //= 10
    return(md)