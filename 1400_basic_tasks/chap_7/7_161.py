from main_funcs imort get_input


def last_team(n:int) -> int:
    ind = 0
    min_num = get_input('Укажите количество набранных очков: ', False)
    for i in range(1, n):
        a = get_input('Укажите количество набранных очков: ', False)
        if a < min_num:
            ind = i
    return(ind)