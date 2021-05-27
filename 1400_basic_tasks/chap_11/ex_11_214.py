from typing import Union


def is_descending(nums:list) -> Union(None, int):
    i = None
    for j in range(len(nums) - 1):
        if nums[j] < nums[j+1]:
            i = j
            break
    return(i)


def print_result(points:list) -> bool:
    i = is_descending(points)
    if i is None:
        return(True)
    else:
        return(False)

