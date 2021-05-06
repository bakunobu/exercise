def max_sec_max_els(nums:list) -> tuple:
    max_el, second_max = max(nums[0], nums[1]), min(nums[0], nums[1])
    if nums[0] > nums[1]:
        max_ind, second_max_ind = 0, 1
    else:
        max_ind, second_max_ind = 1, 0
    
    for i in range(2, len(nums)):
        if nums[i] > second_max:
            if nums[i] > max_el:
                max_el, second_max = nums[i], max_el
                max_ind, second_max_ind = i, max_ind
            else:
                second_max = nums[i]
                second_max_ind = i
    return(max_ind,
           second_max_ind)
    
    
def two_hottest_days(temp:list) -> tuple:
    return(max_sec_max_els(temp))