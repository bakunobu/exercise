import doctest
from typing import Union

def is_in_region_b(x:Union[int, float],
                 y:Union[int, float]) -> bool:
    """
    >>> is_in_region_b(2,3)
    False
    >>> is_in_region_b(4, 5)
    True
    """
    cond = x > 3
    cond = cond and y > 2
    return(cond)


if __name__ == '__main__':
    doctest.testmod()