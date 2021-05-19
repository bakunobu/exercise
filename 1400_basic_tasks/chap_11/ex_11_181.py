def last_to_k(nums:list, k:int) -> list:
    n = nums.pop()
    nums.insert(k-1, n)
    return(nums)