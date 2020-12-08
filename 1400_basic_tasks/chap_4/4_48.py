import doctest


def is_div(a:int, b:int) -> bool:
    """
    >>> is_div(2, 4)
    True
    >>> is_div(1, 3)
    True
    >>> is_div(3, 5)
    False
    """
    cond = not a % b
    cond = cond or not b % a
    return(cond)

if __name__ == "__main__":
    doctest.testmod()