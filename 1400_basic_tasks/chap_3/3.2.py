import doctest


def kg_to_cent(kg:int) -> int:
    """
    >>> kg_to_cent(100)
    1
    >>> kg_to_cent(302)
    3
    >>> kg_to_cent(50)
    0
    
    """
    return(kg//100)


if __name__ == '__main__':
    doctest.testmod()