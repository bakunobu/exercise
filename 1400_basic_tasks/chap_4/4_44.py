import doctest
from typing import Union


def is_in_region(x:Union[int, float],
                 y:Union[int, float]) -> bool:
    """
    >>> is_in_region(6,3)
    True
    >>> is_in_region(4, 2)
    False
    >>> is_in_region(-6, -12)
    True
    """
    cond = x > 5
    cond = cond or x < -1
    return(cond)


if __name__ == "__main__":
    doctest.testmod()