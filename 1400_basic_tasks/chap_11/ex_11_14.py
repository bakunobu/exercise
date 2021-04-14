def num_to_list(n:int) -> list:
    nums = []
    while n:
        x = n % 10
        nums.append(x)
        n //= 10
    return(nums)
