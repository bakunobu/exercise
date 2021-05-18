def first_to_k(nums:list, k:int) -> list:
    f = nums.pop(0)
    nums.insert(k, f)
    return(nums)