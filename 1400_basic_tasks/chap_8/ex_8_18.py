def calc_func(x:float, y:float) -> float:
    y_i = 0.5 * (y + x / (y -1))
    return(y_i)


def calc_first_cond(x:float, a:float, eps:float) -> int:
    prev_y = a
    i = 0
    while True:
        y = calc_func(x, prev_y)
        if abs(y - prev_y) < eps:
            return(i)
        else:
            i += 1
            prev_y = y
    