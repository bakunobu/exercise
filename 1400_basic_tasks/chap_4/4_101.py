import doctest


# a

def find_greater(a:float, b:float, c:float) -> float:
    """
    >>> find_greater(1.0, 2.0, 3.0)
    3.0
    >>> find_greater(3.0, 2.0, 1.0)
    3.0
    >>> find_greater(2.0, 3.0, 1.0)
    3.0
    """
    if a > b and b > c:
        return(a)
    if b > a and a > c:
        return(b)
    return(c)


# b
def find_greater(a:float, b:float, c:float) -> float:
    if a < b and b < c:
        return(a)
    if b < a and a < c:
        return(b)
    return(c)

if __name__ == "__main__":
    doctest.testmod()