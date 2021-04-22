def max_med_el(nums:list) -> int:
    triplets = [(nums[i],
                 nums[i+1],
                 nums[i+2]) for i in range(len(nums) - 2)]
    cond = [1 for x in triplets if x[1] > x[0] and x[1] > x[2]]
    return(len(cond))



