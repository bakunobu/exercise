import doctest


def find_digits(a:int, b:int) -> tuple:
    """
    >>> find_digits(133, 44)
    (1, 7, 7)
    >>> find_digits(412, 24)
    (4, 3, 6)
    """
    num = a + b
    hund = num // 100
    num %= 100
    tens = num // 10
    units = num % 10
    return(hund, tens, units)



if __name__ == "__main__":
    doctest.testmod()