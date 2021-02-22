def loc_max() -> int:
    nums = [int(x) for x in input().split(' ')]
    num_max = 0
    for i in range(1, len(nums)):
        if nums[i-1] < nums[i] > nums[i+1]:
            num_max += 1
    return(num_max)
    
    
print(loc_max())