import doctest


def which_light(t:int) -> str:
    """
    >>> which_light(2)
    'Green'
    >>> which_light(7)
    'Green'
    >>> which_light(9)
    'Red'
    >>> which_light(62)
    'Green'
    """
    t %= 60
    per = t % 5
    if per < 3:
        return('Green')
    else:
        return('Red')
    
if __name__ == '__main__':
    doctest.testmod()