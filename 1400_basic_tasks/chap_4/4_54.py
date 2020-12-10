import doctest

# a
def is_four_in(a: int) -> bool:
    """
    >>> is_four_in(4321)
    True
    >>> is_four_in(5321)
    False
    """
    nums = list(str(a))
    return('4' in nums)


# b
def is_b_in(a: int, b:int) -> bool:
    '''
    >>> is_b_in(4321, 4)
    True
    >>> is_b_in(5321, 7)
    False
    '''
    nums = list(str(a))
    return(str(b) in nums)    

if __name__ == "__main__":
    doctest.testmod()