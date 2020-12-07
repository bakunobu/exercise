import doctest
from typing import Union

# a
def is_in_region(x:Union[int, float],
                 y:Union[int, float]) -> bool:
    """
    >>> is_in_region(3, 3)
    True
    >>> is_in_region(4, 1)
    False
    >>> is_in_region(-3, -3)
    False
    """
    cond_1 = x > 2
    cond_2 = y > 2
    return(cond_1 and cond_2)

# b
def is_in_region_b(x:Union[int, float],
                 y:Union[int, float]) -> bool:
    """
    >>> is_in_region_b(1,2)
    False
    >>> is_in_region_b(-3, -5)
    True
    """
    cond = x < -2
    cond = cond and y < -4
    return(cond)


if __name__ == '__main__':
    doctest.testmod()