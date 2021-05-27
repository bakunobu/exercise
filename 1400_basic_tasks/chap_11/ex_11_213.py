from typing import Union


def is_descending(nums:list) -> Union(None, int):
    i = None
    for j in range(len(nums) - 1):
        if nums[j] < nums[j+1]:
            i = j
            break
    return(i)


def print_result(heiths:list) -> None:
    i = is_descending(heiths)
    if i is None:
        print('Да')
    else:
        print('Нет')

