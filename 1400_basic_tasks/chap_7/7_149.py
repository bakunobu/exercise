from main_funcs import get_input


def calc_interval(n:int) -> bool:
    msg = 'Укажите массу ученика '
    weights = [get_input(msg) for x in range(n)]
    return((max(weights) / min(weights)) > 2)