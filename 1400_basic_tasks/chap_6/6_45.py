# a
def max_indexing(n:int) -> tuple:
    i = 0
    md = 0
    mdi = 0
    while n:
        num = n % 10
        if num > md:
            md = num
            mdi = i
        n //= 10
        i += 1
    return(mdi, i - 1 - mdi)


# b
def min_indexing(n:int) -> tuple:
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
    return(mdi, i - 1 - mdi)

