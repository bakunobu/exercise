from typing import Union


def insert_el(nums:list, s:Union[int, float],
              k:int) -> list:
    n = nums.pop(s)
    nums.insert(k, n)
    return(nums)