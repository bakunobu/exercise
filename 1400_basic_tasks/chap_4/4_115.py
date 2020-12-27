def sum_pos_six(a:float, b:float, c:float,
                d:float, e:float, f:float) -> float:
    res = [x if x > 0 else 0 for x in (a, b, c, d, e, f)]
    return(sum(res))