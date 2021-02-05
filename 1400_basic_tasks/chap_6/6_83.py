import doctest


def is_ascending(n:int) -> bool:
    prev_num = n % 10
    while n > 10:
        n //= 10
        num = n % 10
        if num > prev_num:
            return(False)
        else:
            prev_num = num
    return(True)


def is_descending(n:int) -> bool:
    prev_num = n % 10
    while n > 10:
        n //= 10
        num = n % 10
        if num < prev_num:
            return(False)
        else:
            prev_num = num
    return(True)


def is_sorted(n:int) -> bool:
    """
    >>> is_sorted(13579)
    True
    >>> is_sorted(76520)
    True
    >>> is_sorted(76528)
    False
    """
    return(is_ascending(n) or is_descending(n))




if __name__ == '__main__':
    doctest.testmod()