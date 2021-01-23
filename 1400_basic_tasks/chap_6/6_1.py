import doctest

# a
def floor_div(a:int, b:int) -> int:
    """
    >>> floor_div(2, 3)
    1
    >>> floor_div(2, 4)
    2
    >>> floor_div(10, 3)
    0
    >>> floor_div(2, 7)
    3
    """
    res = 0
    while a <= b:
        b -= a
        res += 1
        
    return(res)


# b
def div_mod(a:int, b:int) -> int:
    """
    >>> div_mod(2, 7)
    1
    >>> div_mod(10, 3)
    3
    >>> div_mod(2, 8)
    0
    >>> div_mod(4, 10)
    2
    """

    while a <= b:
        b -= a
    return(b)

if __name__ == '__main__':
    doctest.testmod()