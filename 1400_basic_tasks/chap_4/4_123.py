def points_to_res(x:int) -> str:
    if x == 3:
        return('Win')
    elif x == 0:
        return('Lose')
    else:
        return('Draw')