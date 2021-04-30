from typing import Union


# a
def max_el(nums:list) -> Union[int, float]:
    return(max(nums))


# b
def min_el(nums:list) -> Union[int, float]:
    return(min(nums))


# c
def min_max_diff(nums:list) -> Union[int, float]:
    return(max(nums) - min(nums))

# d
def max_el_ind(nums:list) -> int:
    return(nums.index(max(nums)))


# e
def min_max_index(nums:list) -> tuple:
    min_ind = nums.index(max(nums))
    max_ind = nums.index(min(nums))
    return(min_ind, max_ind)