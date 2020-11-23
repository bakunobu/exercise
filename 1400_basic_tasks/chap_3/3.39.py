import doctest

def restore_num(n:int) -> int:
    """
    >>> restore_num(456)
    465
    """
    n = 456
    mid_dig = n %10
    n //= 10
    first_dig = n // 10
    last_dig =  n % 10

    n = last_dig + mid_dig * 10 + first_dig * 100
    return(n)


def rest_dig_input() -> int:
    n = int(input())
    return(restore_dig(n))



if __name__ == "__main__":
    doctest.testmod()