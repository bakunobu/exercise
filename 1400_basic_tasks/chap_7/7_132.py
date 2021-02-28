from main_funcs import get_input


def num_els(n:int=30) -> int:
    nums = []
    for _ in range(n):
        a = get_input('Введите число: ')
        if a not in nums:
            nums.append(a)
    return(len(nums))