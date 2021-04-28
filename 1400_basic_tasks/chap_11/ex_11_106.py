def two_same_els(nums:list) -> bool:
    return(len(nums) - len(set(nums)) == 1)