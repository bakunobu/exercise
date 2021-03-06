from main_funcs import get_input


# a
def count_max(n:int) -> int:
    msg = 'Введите число: '
    nums = [get_input(msg, False) for _ in range(n)]
    max_num = max(nums)
    return(nums.count(max_num))


# b
def count_min(n:int) -> int:
    msg = 'Введите число: '
    nums = [get_input(msg, False) for _ in range(n)]
    min_num = min(nums)
    return(nums.count(min_num))