def calc_ser_el(el_1:float, el_2:float,
                el_3:float, i:int) -> float:
    eq_1 = (i - 1) / (i ** 2 + 1) * el_3
    eq_2 = eq_1 - el_2 + el_1
    return(eq_2)


def calc_series_els(n:int) -> float:
    els = [0, 0, 1.5,]
    for i in range(3, n+1):
        el = calc_ser_el(els[i-3], els[i-2], els[i-1],i)
        els.append(el)
    return(els[-1])
