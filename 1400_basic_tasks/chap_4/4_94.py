import doctest

def find_digit(k:int) -> int:
    """
    >>> find_digit(1)
    1
    >>> find_digit(2)
    0
    >>> find_digit(3)
    1
    >>> find_digit(178)
    8
    >>> find_digit(179)
    9
    >>> find_digit(180)
    9
    """
    i = (k // 2) // 10
    j = ((k-1) // 2) % 10
    if k % 2:
        return(i+1)
    else:
        return(j)
    
if __name__ == "__main__":
    doctest.testmod()