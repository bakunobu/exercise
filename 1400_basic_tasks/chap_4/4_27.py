import doctest


def sum_cubes(a:int) -> bool:
    """
    >>> sum_cubes(48)
    True
    >>> sum_cubes(52)
    False
    """
    tens = a // 10
    units = a % 10
    total = 4 * (tens ** 3 + units ** 3)
    return(total == a ** 2)



if __name__ == '__main__':
    doctest.testmod()