from main_funcs import get_input


def calc_interval(n:int) -> bool:
    msg = 'Укажите целое число: '
    nums = [get_input(msg, False) for x in range(n)]
    return((max(nums) - min(nums)) <= 25)