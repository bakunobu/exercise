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


def cold_second_cold(temper:list) -> tuple:
    return(min_sec_min_els(temper))