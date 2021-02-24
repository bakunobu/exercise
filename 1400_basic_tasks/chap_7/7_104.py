from main_funcs import get_iput


def seq_team_points(n:int) -> bool:
    a_0 = get_input('Введите число: ', False)
    for _ in range(n-1):
        a = get_input('Введите число: ', False)
        if a_0 != a:
            return(False)
    return(True)