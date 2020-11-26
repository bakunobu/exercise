def kmh_to_ms(km: float) -> float:
    return(km * 1000 / 3600)


def which_faster(km:float, m:float) -> float:
    m_2 = kmh_to_ms(km)
    if m_2 > m:
        return(km)
    else:
        return(m)