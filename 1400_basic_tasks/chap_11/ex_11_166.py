from typing import Any

# a
def insert_el(nums:list, ind:int=1, el:Any=10) -> list:
    nums.insert(ind, el)
    return(nums)


# b
def insert_el(nums:list, ind:int, el:Any=100) -> list:
    nums.insert(ind, el)
    return(nums)