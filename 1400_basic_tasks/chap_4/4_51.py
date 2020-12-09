import doctest


def decompose(a:int) -> tuple:
    hund = a // 100
    a -= hund * 100
    tens = a // 10
    units = a % 10
    return(hund, tens, units)


# a
def is_six(a: int) -> bool:
    """
    >>> is_six(643)
    True
    >>> is_six(543)
    False
    
    """
    nums = decompose(a)
    return(6 in nums)
    

def is_n(a: int,
         n: int) -> bool:
    """
    >>> is_n(643, 6)
    True
    >>> is_n(643, 5)
    False
    """
    nums = decompose(a)
    return(n in nums)
    
if __name__ == "__main__":
    doctest.testmod()