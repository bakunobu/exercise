import doctest


def slice_rect(a: int,l:int) -> int:
    """
    >>> slice_rect(300, 150)
    2
    >>> slice_rect(300, 160)
    1
    >>> slice_rect(900, 300)
    3
    """
    return(a // l)


if __name__ == "__main__":
    doctest.testmod()