# a
def sum_even_els(nums:list, a:int=2) -> int:
    cond_els = [x for x in nums if not x % a]
    return(sum(cond_els))


# b
def sum_div_els(nums:list, a:int) -> int:
    cond_els = [x for x in nums if not x % a]
    return(sum(cond_els))


# c
def sum_any_div(nums:list, a:int, b:int) -> int:
    list_a = sum_div_els(nums, a)
    list_b = sum_div_els(nums, b)
    list_b = [x for x in list_b if x not in list_a]
    return(sum(list_a) + sum(list_b))