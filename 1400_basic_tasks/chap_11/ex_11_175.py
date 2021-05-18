from typing import Union


def sign(x:Union[int, float]) -> int:
    if x < 0:
        return(-1)
    elif x > 0:
        return(1)
    else:
        return(0)
    
    
def add_num(nums:list, n:Union[int, float]) -> list:
    i = 0
    while i < len(nums) - 1:
        if sign(nums[i]) == sign(nums[i + 1]):
            nums.insert(i+1, n)
            i += 1
        i += 1
    return(nums)