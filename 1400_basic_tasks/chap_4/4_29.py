import doctest


# a
def div_three(a:int) -> bool:
    """
    >>> div_three(19)
    False
    >>> div_three(18)
    True
    """
    return(not a % 3)

# b
def div_a(num:int, a:int) -> bool:
    """
    >>> div_a(18, 3)
    True
    >>> div_a(26, 4)
    True
    >>> div_a(24, 4)
    False
    """
    tens = num // 10
    units = num % 10
    return(not (tens + units) % a)
    

if __name__ == '__main__':
    doctest.testmod()