def remove_min_max(nums:list) -> list:
    nums.remove(max(nums))
    nums.remove(min(nums))
    return(nums)