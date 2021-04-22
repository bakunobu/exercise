def count_els(nums:list) -> tuple:
    even = len([x for x in nums if not x % 2])
    fives = len([x for x in nums if not x % 5])
    return(even, fives)