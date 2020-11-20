import doctest


def h_d_n(x:int) -> tuple:
    """
    >>> h_d_n(123)
    (1, 2, 3)
    >>> h_d_n(321)
    (3, 2, 1)
    >>> h_d_n(90)
    (0, 9, 0)
    """
    return(x // 100, (x % 100) // 10, x % 10)
  

if __name__ == "__main__":
    doctest.testmod()