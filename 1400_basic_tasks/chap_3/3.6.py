import doctest


def num_seat(n: int) -> int:
    """
    >>> num_seat(1)
    1
    >>> num_seat(5)
    2
    >>> num_seat(8)
    2
    >>> num_seat(9)
    3
    >>> num_seat(36)
    9
    >>> num_seat(37)
    Out of range
    
    """
    if n < 1 or n > 36:
        print('Out of range')
        return(None)
    else:
        if n % 4 == 0:
            return(n // 4)
        else:
            return(1 + n // 4)


if __name__ == "__main__":
    doctest.testmod()