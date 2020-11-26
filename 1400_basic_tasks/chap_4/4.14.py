def calc_ind(R:float, U:float) -> float:
    return(R * U)


def comp_ind(a:tuple, b:tuple) -> tuple:
    I_1 = calc_ind(* a)
    I_2 = calc_ind(* b)
    if I_1 > I_2:
        return(a)
    else:
        return(b)