from typing import Union


# a
def is_even(x) -> bool:
    return(not x % 2)


def first_odd(nums:list) -> Union[int, None]:
    i = 0
    while i < len(nums) - 1:
        if not is_even(nums[i]):
            return(i)
        i += 1
    
    return(None)


def print_first_odd_ind(nums:list) -> None:
    i = first_odd(nums)
    if i is None:
        print('Нечетных элементов в массиве нет!')
    else:
        print(i)
        
        
# b
def div_by_n(x:int, n:int=13) -> bool:
    return(not x % n)


def first_cond_num(nums:list) -> Union[int, None]:
    i = 0
    while i < len(nums) - 1:
        if div_by_n(nums[i]):
            return(i)
        i += 1
    
    return(None)


def print_first_cond_ind(nums:list) -> None:
    i = first_cond_num(nums)
    if i is None:
        print(f'Чисел, делящхся на 13, в массиве нет!')
    else:
        print(i)
        