import doctest


def find_digit(n:int) -> int:
    """
    >>> find_digit(1)
    0
    >>> find_digit(2)
    1
    >>> find_digit(10)
    9
    >>> find_digit(11)
    1
    >>> find_digit(31)
    2
    >>> find_digit(32)
    0
    """
    if n <= 10:
        return(n-1)
    else:
        
        



if __name__ == "__main__":
    doctest.testmod()