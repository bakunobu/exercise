from main_funcs import get_iput


def seq_team_points() -> bool:
    a_0 = get_input('Введите число: ', False)
    while True:
        a = get_input('Введите число: ', False)
        if a < 0:
            break
        if a_0 != a:
            return(False)
    return(True)