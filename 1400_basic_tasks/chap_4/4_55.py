# a

def is_two_in(a: int) -> bool:
    num = list(str(a))
    nums = set(num)
    set_num = nums.intersection({'2', '7'})
    return(bool(len(set_num)))

# b
def is_three_in(a: int) -> bool:
    num = list(str(a))
    nums = set(num)
    set_num = nums.intersection({'3', '6', '9'})
    return(bool(len(set_num)))