import math
import doctest


def abs_value(a:float) -> float:
    """
    >>> abs_value(-2.3)
    2.3
    >>> abs_value(2.0)
    2.0
    """
    return(math.sqrt(a ** 2))


def abs_value_alt(a:float) -> float:
    """
    >>> abs_value_alt(-2.3)
    2.3
    >>> abs_value_alt(147.425)
    147.425
    """
    if a < 0:
        return(-a)
    return(a)


if __name__ == "__main__":
    doctest.testmod()