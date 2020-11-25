def foot_to_m(f:float) -> float:
    return(f * 0.3048)


def foot_to_km(f:float) -> float:
    m = foot_to_m(f)
    return(m / 1000)


def which_bigger(km:float, f:float) -> float:
    km_2 = foot_to_km(f)
    if km > km_2:
        return(km)
    else:
        return(f)