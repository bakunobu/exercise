from main_funcs import get_input


def max_temp(n:int=30) -> float:
    max_temp = get_input('Укажите температуру: ')
    for _ in range(1, n):
        t = get_input('Укажите температуру: ')
        if t > max_temp:
            max_temp = t
    return(max_temp)