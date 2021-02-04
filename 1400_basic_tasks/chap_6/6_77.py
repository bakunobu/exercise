import doctest


# a
def all_eq(n:int) -> bool:
    """
    >>> all_eq(666)
    True
    >>> all_eq(669)
    False
    >>> all_eq(77777777)
    True
    """
    prev_num = n % 10
    while n > 10:
        n //= 10
        num = n % 10
        if num != prev_num:
            return(False)
        else:
            prev_num = num
    return(True)


# b
def pair_eq(n:int) -> bool:
    """
    >>> pair_eq(35510)
    True
    >>> pair_eq(679)
    False
    >>> pair_eq(278882)
    True
    """
    prev_num = n % 10
    while n > 10:
        n //= 10
        num = n % 10
        if num == prev_num:
            return(True)
        else:
            prev_num = num
    return(False)


if __name__ == '__main__':
    doctest.testmod()
