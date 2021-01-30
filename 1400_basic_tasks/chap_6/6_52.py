# a

def if_three_in(n:int) -> bool:
    while n:
        num = n % 10
        if num == 3:
            return(True)
        n //= 10
    return(False)


# b
def if_nums_in(n:int, *args) -> bool:
    while n:
        num = n % 10
        if num in args:
            return(True)
        n //= 10
    return(False)

