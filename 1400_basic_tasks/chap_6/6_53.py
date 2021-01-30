# a
def if_nums_in(n:int, a:int) -> bool:
    while n:
        num = n % 10
        if num == a:
            return(True)
        n //= 10
    return(False)


# b
def if_nums_in(n:int, b:int) -> bool:
    while n:
        num = n % 10
        if num == b:
            return(False)
        n //= 10
    return(True)


# c
def if_nums_in(n:int, a:int, k:int) -> bool:
    counter = 0
    while n:
        num = n % 10
        if num == a:
            counter += 1
        n //= 10
    return(counter > k)


# d
def if_nums_in(n:int, *args) -> bool:
    while n:
        num = n % 10
        if num in args:
            return(True)
        n //= 10
    return(False)