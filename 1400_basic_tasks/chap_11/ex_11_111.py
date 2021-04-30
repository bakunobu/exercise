def length_even_nums(nums:list) -> int:
    i = 0
    longest = 0
    for x in nums:
        if x % 2:
            i += 1
        else:
            longest = max(i, longest)
            i = 0
    return(longest)
