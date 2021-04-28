from typing import Union


def sign(x:Union[int, float]) -> int:
    if x > 0:
        return(1)
    elif x < 0:
        return(-1)
    else:
        return(0)
    
    
def change_sign(nums:list) -> int:
    s = 0
    for i in range(len(nums) - 1):
        if sign(nums[i]) != sign(nums[i+1]):
            s += 1
    return(s)


