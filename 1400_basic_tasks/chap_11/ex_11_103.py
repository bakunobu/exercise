def max_sum_five(nums:list) -> list:
    five_nums = nums[:5]
    max_sum = sum(nums[:5])
    for i in range(1, len(nums) - 5):
        if sum(nums[i:i+5]) > max_sum:
            max_sum = sum(nums[i:i+5])
            five_nums = nums[i:i+5]
    return(five_nums)