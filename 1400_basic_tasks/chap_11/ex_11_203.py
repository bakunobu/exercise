from typing import Union


def find_els(nums:list, n:Union[int, float]) -> None:
    i = None
    for j in range(len(nums)):
        if nums[j] > n:
            i = j + 1
            print(* nums[i:], sep=', ')
            break
    if i is None:
        print('Таких чисел в массиве не содержится!')