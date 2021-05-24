from typing import Union


def find_first_a(nums:list, a:Union[int, float]) -> Union[int, None]:
    try:
        i = nums.index(a)
    except ValueError:
        i = None
    return(i)


def print_all_els(nums:list, a:Union[int, float]) -> None:
    i = find_first_a(nums, a)
    if i is not None:
        print(* nums[:i], sep=', ', end=', ')
        print(* nums[i+1:],  sep=', ')
    else:
        print('Таких элементов нет!')




