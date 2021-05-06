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
    

def oldest_pers(years:list) -> tuple:
    return(min_second_min(years))