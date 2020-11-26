def calc_dens(m: float, V:float) -> float:
    return(m/V)


def comp_dens(a: tuple, b:tuple) -> tuple:
    d_1 = calc_dens(* a)
    d_2 = calc_dens(* b)
    if d_1 > d_2:
        return(a)
    else:
        return(b)