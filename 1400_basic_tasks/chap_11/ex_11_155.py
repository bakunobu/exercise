def min_max_shift(nums:list) -> list:
    i = None # index of first neg
    j = None # index of last pos
    for _ in range(len(nums)):
        if nums[_] < 0:
            if i is None:
                i = _
        elif nums[_] > 0:
            j = _
    if i and j:
        nums[i], nums[j] = nums[j], nums[i]
    else:
        print('Condition not met, returns exact list.')
    return(nums)