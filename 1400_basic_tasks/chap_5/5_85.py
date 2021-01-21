def sum_a_b(a:int, b:int) -> int:
    nums = [x for x in range(a, b+1) if x % 4 == 0]
    return(sum(nums))