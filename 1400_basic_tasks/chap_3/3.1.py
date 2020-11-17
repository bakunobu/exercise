import doctest


def cm_to_meter(cm:int) -> int:
    """
    
    >>> cm_to_meter(100)
    1
    >>> cm_to_meter(102)
    1
    >>> cm_to_meter(3000)
    30
    >>> cm_to_meter(90)
    0
    
    """
    return(cm // 100)


if __name__ == '__main__':
    doctest.testmod()