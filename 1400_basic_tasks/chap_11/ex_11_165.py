# a
def drop_duplicates(nums:list) -> list:
    return(list(set(nums)))


# b
def drop_duplicates_order(nums:list) -> list:
    orig_nums = []
    for x in nums:
        if x not in orig_nums:
            orig_nums.append(x)
    return(orig_nums)