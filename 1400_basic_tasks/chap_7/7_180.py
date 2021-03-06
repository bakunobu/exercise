from main_funcs import get_input


def count_min_temp(n:int=30) -> int:
    msg = 'Укажите среднесуточную температуру: '
    nums = [get_input(msg) for _ in range(n)]
    min_num = min(nums)
    return(nums.count(min_num))