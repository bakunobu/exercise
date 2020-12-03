import doctest

# a 
def greater_nine(a: int) -> bool:
    """
    >>> greater_nine(19)
    True
    >>> greater_nine(34)
    False
    """
    tens = a // 10
    units = a % 10
    
    return(tens+units > 9)

# b
def greater_a(num: int, a: int) -> bool:
    """
    >>> greater_a(49, 11)
    True
    >>> greater_a(34, 37)
    False
    """
    tens = num // 10
    units = num % 10
    
    return(tens+units > a)

if __name__ == '__main__':
    doctest.testmod()