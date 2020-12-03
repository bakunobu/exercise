import doctest


def square_sum_cube(a: int) -> bool:
    """
    >>> square_sum_cube(111)
    False
    """
    b = a
    hund = a // 100
    a -= hund * 100
    tens = a // 10
    units = a % 10
    return(hund ** 3 + tens ** 3 + units ** 3 == b ** 2) 


if __name__ == '__main__':
    doctest.testmod()