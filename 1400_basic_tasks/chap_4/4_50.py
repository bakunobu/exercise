import doctest


# a
def is_cont_four_seven(x:int) -> bool:
    tens = x // 10
    units = x % 10
    cond = tens == 4
    cond = cond or tens == 7
    cond = cond or units == 4
    cond = cond or units == 7
    return(cond)



# b
def is_cont_some_of_three(x:int) -> bool:
    """
    >>> is_cont_some_of_three(42)
    False
    >>> is_cont_some_of_three(43)
    True
    """
    tens = x // 10
    units = x % 10
    set_a = {tens, units}
    set_b = {3, 6, 9}
    set_c = set_a.intersection(set_b)
    return(bool(len(set_c)))


if __name__ == "__main__":
    doctest.testmod()