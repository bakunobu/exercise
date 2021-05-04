# a
def min_max_diff(nums:list) -> bool:
    return(max(nums) - min(nums) <= 25)


# b
def min_max_diff(nums:list) -> bool:
    return(max(nums) / min(nums) >= 2)