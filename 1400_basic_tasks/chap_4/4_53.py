 
def decompose(a:int) -> tuple:
    hund = a // 100
    a -= hund * 100
    tens = a // 10
    units = a % 10
    return(hund, tens, units)



def is_in_it(a: int, example:set) -> bool:
    """
    >>> is_six(643)
    True
    >>> is_six(543)
    False
    
    """
    nums = set(decompose(a))
    set_c = nums.intersection(example)
    return(bool(len(set_c)))

# a
print(is_in_it(643, {4, 7}))
print(is_in_it(653, {4, 7}))
print(is_in_it(643, {3, 6, 9}))