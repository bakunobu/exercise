# a
def count_pos_els(nums:list) -> bool:
    pos_nums = [x for x in nums if x > 0]
    return(len(pos_nums) <= 5)


# b
def wierd_cond(nums:list) -> bool:
    small_nums = [x for x in nums if x <= 50.55]
    return(not len(small_nums) % 4) 