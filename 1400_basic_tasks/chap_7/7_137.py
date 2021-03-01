from main_funcs import get_input


def max_dist(n:int) -> float:
    max_dist = get_input('Укажите расстояние: ')
    for _ in range(1, n):
        dist = get_input('Укажите расстояние: ')
        if dist > max_dist:
            max_dist = dist
    return(max_dist)