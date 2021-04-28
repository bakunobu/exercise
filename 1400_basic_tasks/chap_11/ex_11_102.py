from typing import Union


def closest_neighbour(nums:list) -> Union[int, float]:
    m = sum(nums) / len(nums)
    min_num = abs(m - nums[0])
    for num in nums[1:]:
        if abs(m - num) < min_num:
            min_num = abs(m - num)
    return(min_num)