# a
def dif_from_last(nums:list) -> int:
    cond_nums = [x for x in nums if x != nums[-1]]
    return(len(cond_nums))


# b
def div_by_a(nums:list, a:int) -> int:
    cond_nums = [x for x in nums if not x % 2]
    return(len(cond_nums))