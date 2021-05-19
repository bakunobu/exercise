def s_to_k(nums:list, s:int, k:int) -> list:
    n = nums.pop(s-1)
    nums.insert(k-1, n)
    return(nums)
    