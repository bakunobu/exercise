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


def max_moist(moist:list) -> int:
    max_m = count_max_els(moist)
    return(max_m)
