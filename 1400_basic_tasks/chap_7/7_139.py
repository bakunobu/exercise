from main_funcs import get_input


def max_speed(n:int=20) -> float:
    max_speed = get_input('Укажите максимальную скорость: ')
    for _ in range(1, n):
        v = get_input('Укажите максимальную скорость: ')
        if v > max_speed:
            max_speed = v
    return(max_speed)