import doctest
from typing import Union

def is_div(m:int, n:int) -> Union[int,str]:
    """
    >>> is_div(3, 1)
    3
    >>> is_div(100, 5)
    20
    >>> is_div(-3, 1)
    -3
    >>> is_div(1, 3)
    'm на n нацело не делится'
    """
    if not m%n:
        return(m//n)
    else:
        return('m на n нацело не делится')


if __name__ == "__main__":
    doctest.testmod()