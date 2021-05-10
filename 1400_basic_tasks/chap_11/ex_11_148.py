from typing import Union


def pre_sorter(nums:list) -> Union[int, float]:
    i = 0
    while i < len(nums) - 1:
        if nums[i] > nums[i+1]:
            nums[i], nums[i+1] = nums[i+1], nums[i]
        
        i += 1
            
    return(nums[-1])

"""
nums = [4, 5, 1, 2, 3, 6]

print(pre_sorter(nums))
"""