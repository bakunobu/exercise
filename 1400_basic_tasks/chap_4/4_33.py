import doctest


# a
def is_two_s(a: int) -> bool:
    """
    >>> is_two_s(119)
    True
    >>> is_two_s(971)
    True
    >>> is_two_s(412)
    False
    >>> is_two_s(-761)
    True
    """
    a = abs(a)
    hund = a // 100
    a -= hund * 100
    tens = a // 10
    units = a % 10
    x = hund + tens + units
    return(10 <= x <= 99)


# b
def is_prod_hund(a: int) -> bool:
    """
    >>> is_prod_hund(191)
    False
    >>> is_prod_hund(997)
    True
    """
    a = abs(a)
    hund = a // 100
    a -= hund * 100
    tens = a // 10
    units = a % 10
    x = hund * tens * units 
    return(100 <= x <= 999)

# c
def is_greater_a(num: int, a:int) -> bool:
    """
    >>> is_greater_a(199, 76)
    True
    >>> is_greater_a(999, 999)
    False
    """
    num = abs(num)
    hund = num // 100
    num -= hund * 100
    tens = num // 10
    units = num % 10
    x = hund * tens * units 
    return(x > a)   
    

# d
def is_div_five(a:int) -> bool:
    """
    >>> is_div_five(199)
    False
    >>> is_div_five(190)
    True
    """
    a = abs(a)
    hund = a // 100
    a -= hund * 100
    tens = a // 10
    units = a % 10
    x = hund + tens + units
    return(not x % 5)


# e
def is_div_a(num:int, a:int) -> bool:
    """
    >>> is_div_a(198, 3)
    True
    >>> is_div_a(190, 5)
    True
    >>> is_div_a(845, 2)
    False
    """
    num = abs(num)
    hund = num // 100
    num -= hund * 100
    tens = num // 10
    units = num % 10
    x = hund + tens + units
    return(not x % a)



if __name__ == '__main__':
    doctest.testmod()