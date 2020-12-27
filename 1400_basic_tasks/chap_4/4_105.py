def abs_value(a:float) -> float:
    if a < 0:
        return(-a)
    return(a)


def comp_and_mod(a:float, b:float) -> float:
    if abs_value(a) > abs_value(b):
        return(a / 2)
    return(a)