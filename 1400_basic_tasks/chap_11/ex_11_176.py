def first_to_last(nums:list) -> list:
    f = nums.pop(0)
    nums.append(f)
    return(nums)