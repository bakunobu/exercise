def num_sum(a:int=30, b:int=101) -> int:
    nums = [x for x in range(a, b) if x % 3 == 0 and x % 10 in (2, 4, 8)]
    return(sum(nums))

