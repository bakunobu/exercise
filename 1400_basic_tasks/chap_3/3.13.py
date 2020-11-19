import doctest


def find_line(n:int) -> int:
    """
    >>> find_line(1)
    0
    >>> find_line(6)
    1
    >>> find_line(50)
    9
    """
    return(n // 5 + min(1, n % 5) - 1)


def find_col(n:int) -> int:
    """
    >>> find_col(1)
    0
    >>> find_col(5)
    4
    >>> find_col(6)
    0
    >>> find_col(50)
    4
    """
    my_dict = {1: 0,
               2: 1,
               3: 2,
               4: 3,
               0: 4}
    
    i = n % 5
    return(my_dict[i])


if __name__ == "__main__":
    doctest.testmod()