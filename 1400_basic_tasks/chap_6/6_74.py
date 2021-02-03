import doctest

def is_power(n:int, b:int) -> bool:
    """
    >>> is_power(3, 3)
    True
    >>> is_power(27, 3)
    True
    >>> is_power(36, 3)
    False
    >>> is_power(81, 3)
    True
    """
    while n > b:
        n /= b
    if n == b:
        return(True)
    else:
        return(False)


def is_power_three(n:int, b:int=3) -> bool:
    return(is_power(n, b))


def is_power_five(n:int, b:int=5) -> bool:
    return(is_power(n, b))


if __name__ == '__main__':
    doctest.testmod()