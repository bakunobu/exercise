# a
def max_digit(n:int) -> int:
    md = 0
    while n:
        num = n % 10
        if md < num and md % 2 == 0:
            md = num
        n //= 10
    return(md)

# b
def min_indexing(n:int) -> int:
    i = 0
    md = 9
    mdi = 0
    while n:
        num = n % 10
        if num < md:
            md = num
            mdi = i
        n //= 10
        i += 1
    return(i - 1 - mdi)
