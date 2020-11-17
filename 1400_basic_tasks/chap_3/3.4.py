import doctest

def share_apples(pupils:int, apples:int) -> tuple:
    """
    >>> share_apples(2, 3)
    (1, 1)
    >>> share_apples(2, 6)
    (3, 0)
    >>> share_apples(3, 11)
    (3, 2)
    """
    return(apples//pupils, apples%pupils)



if __name__ == "__main__":
    doctest.testmod()