import doctest


def which_floor(n:int) -> int:
    """
    >>> which_floor(17)
    Out of range
    >>> which_floor(1)
    1
    >>> which_floor(15)
    5
    >>> which_floor(8)
    3
    """
    if n < 1 or n > 15:
        print('Out of range')
        return(None)
    else:
        if n % 3 == 0:
            return(n // 3)
        else:
            return(1 + n // 3)



if __name__ == "__main__":
    doctest.testmod()