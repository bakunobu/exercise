import math

def greater_square(n:int) -> int:
    i = int(math.sqrt(n)) + 1
    return(i)


def while_loop_greater_square(n:int) -> int:
    i = 1
    while i ** 2 <= n:
        i += 1
    return(i)

