# a
def max_second_max(nums:list) -> tuple:
    max_el = None
    second_el = None
    for num in nums:
        if max_el is None:
            max_el = num
        elif second_el is None:
            max_el, second_el = max(num, max_el), min(num, max_el)
        elif num > second_el:
            max_el, second_el = max(num, max_el), min(num, max_el)
        else:
            continue
    
    return(max_el,
           second_el)
    

# b
def min_second_min(nums:list) -> tuple:
    min_el = None
    second_min = None
    for num in nums:
        if min_el is None:
            min_el = num
        elif second_min is None:
            min_el, second_min = min(min_el, num), max(min_el, num)
        elif num < second_min:
            min_el, second_min = min(min_el, num), max(min_el, num)
    
    return(min_el,
           second_min)
    

# c
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

# d
def min_sec_min_els(nums:list) -> tuple:    
    min_el = nums[0]
    min_ind = 0
    second_min = None
    second_min_ind = None
    for i in range(1, len(nums)):
        if second_min is None:
            if nums[i] < min_el:
                min_el, second_min = nums[i], min_el
                min_ind, second_min_ind = 1, 0
            else:
                second_min = nums[i]
                second_min_ind = i
        elif nums[i] < min_el:
            if nums[i] < min_el:
                min_el, second_min = nums[i], min_el
                min_ind, second_min_ind = 1, 0
            else:
                second_min = nums[i]
                second_min_ind = i
                
            
    return(min_ind,
           second_min_ind)