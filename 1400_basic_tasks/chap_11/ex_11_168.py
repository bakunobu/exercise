from typing import Any
from typing import Union


def insert_el(nums:list, ind:int, el:Any=100) -> list:
    nums.insert(ind, el)
    return(nums)


def add_mount_info(mountains:list, i:int, h:Union[int, float]) -> list:
    new_list = insert_el(mountains, i, h)
    return(new_list)