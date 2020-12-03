import doctest


# a
def which_bigger(a:int) -> str:
    """
    >>> which_bigger(17)
    'Units'
    >>> which_bigger(71)
    'Tens'
    >>> which_bigger(11)
    'Equal'
    """
    tens = a // 10
    units = a % 10
    if tens > units:
        return('Tens')
    elif tens < units:
        return('Units')
    else:
        return('Equal')
    

# b
def ends_seven(a: int) -> bool:
    """
    >>> ends_seven(17)
    True
    >>> ends_seven(71)
    False
    >>> ends_seven(11)
    False
    """
    return(a % 10 == 7)


if __name__ == '__main__':
    doctest.testmod()