# a
def is_positive(nums:list) -> bool:
    cond_nums = [x for x in nums if x > 20]
    return(sum(cond_nums) > 100)


# b
def is_even(nums:list) -> bool:
    cond_nums = [x for x in nums if x < 50]
    return(not sum(cond_nums) % 2)