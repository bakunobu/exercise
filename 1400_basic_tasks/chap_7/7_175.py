from main_funcs import get_input


def sort_points(n:int=4) -> list:
    msg = 'Укажите время участника: '
    scores = [get_input(msg, False) for _ in range(n)]
    return(sorted(scores)[:4])