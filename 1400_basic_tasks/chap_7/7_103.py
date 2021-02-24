from main_funcs import get_iput


def seq_team_points(n:int) -> bool:
    a_0 = get_input('Укажите количество очков: ', False)
    for _ in range(n-1):
        a = get_input('Укажите количество очков: ', False)
        if a_0 <= a:
            return(False)
        a_0 = a
    return(True)