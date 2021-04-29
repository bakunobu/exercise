from typing import Union


def seq_el(nums:list) -> Union[int, float]:
    seq_num = nums[0]
    for el in nums[1:]:
        if seq_num == el:
            return(el)
        seq_num = el
        
        
def unique_nums(nums:list) -> int:
    return(len(set(nums)))