def last_to_first(nums:list) -> list:
    l = nums.pop()
    nums.insert(0, l)
    return(nums)