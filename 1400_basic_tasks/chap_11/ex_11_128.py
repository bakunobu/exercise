def count_min_els(nums:list) -> int:
    counter = 0
    min_el = None
    for num in nums:
        if min_el is None:
            counter += 1
            min_el = num
        elif num < min_el:
            min_el = num
            counter = 1
        elif num == min_el:
            counter += 1
        else:
            pass
    return(counter)


def min_temp(temp:list) -> int:
    min_t  = count_min_els(temp)
    return(min_t)