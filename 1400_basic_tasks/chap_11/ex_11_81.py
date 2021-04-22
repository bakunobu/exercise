def count_even_pairs(nums:list) -> int:
    counter = 0
    for i in range(len(nums)-1):
        if not nums[i] % 2:
            if not nums[i + 1] % 2:
                counter += 1
    return(counter)
