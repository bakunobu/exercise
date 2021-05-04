# a
def count_max_els(nums:list) -> int:
    counter = 0
    max_el = None
    for num in nums:
        if max_el is None:
            counter += 1
            max_el = num
        elif num > max_el:
            max_el = num
            counter = 1
        elif num == max_el:
            counter += 1
        else:
            pass
    return(counter)

# b
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