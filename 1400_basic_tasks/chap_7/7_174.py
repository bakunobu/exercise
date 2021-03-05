from main_funcs import get_input


def sort_points(n:int=12) -> list:
    msg = 'Введите количество очков: '
    scores = [get_input(msg, False) for _ in range(n)]
    return(sorted(scores)[:3])