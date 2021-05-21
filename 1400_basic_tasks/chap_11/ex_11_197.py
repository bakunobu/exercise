from typing import Union


# a
def print_prev_els(nums:list, n:Union[int, float]) -> None:
    dummy = nums[:]
    while dummy:
        d = dummy.pop(0)
        if d == n:
            break
        else:
            print(d, end=',')
            
            
# b
def ends_with(x:int, ld:int=7) -> bool:
    return(not x % ld)


def find_last(nums:list, ld:int=7) -> Union[int, None]:
    i = len(nums) - 1
    while i > 0:
        if ends_with(nums[i], ld):
            return(i)
        i -=1
    return(None)
    
    
def print_after(nums:list) -> None:
    i = find_last(nums, 7)
    if i is not None:
        print(* nums[i+1:], sep=', ')