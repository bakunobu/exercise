def count_even_pairs(nums:list) -> int:
    counter = 0
    for i in range(len(nums)-1):
        if not nums[i] % 10:
            if not nums[i + 1] % 10:
                counter += 1
    return(counter)
