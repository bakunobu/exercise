def num_to_list(n:int) -> list:
    units = []
    while n:
        u = n % 10
        n //= 10
        units.append(u)
    return(units)


def unique_units(n:int) -> int:
    nums = num_to_list(n)
    return(len(set(nums)))
