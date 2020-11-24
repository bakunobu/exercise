import doctest


def find_digits(a:int, b:int) -> tuple:
    """
    >>> find_digits(33, 44)
    (7, 7)
    >>> find_digits(12, 24)
    (3, 6)
    """
    num = a + b
    tens = num // 10
    units = num  10
    return(tens, units)



if __name__ == "__main__":
    doctest.testmod()