import doctest


def found_digits(a: int, b: int) -> tuple:
    """
    >>> found_digits(38,1)
    (3, 9)
    >>> found_digits(54,7)
    (6, 1)
    """
    tens = (a+b) // 10
    units = (a+b) % 10
    return(tens, units)



if __name__ == "__main__":
    doctest.testmod()