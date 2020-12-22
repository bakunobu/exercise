def years_total(y_1:int, m_1:int, d_1:int,
                y:int=2020, m:int=12, d:int=22) -> int:
    if d < d_1:
        m -= 1
    if m < m_1:
        y -= 1
    return(y - y_1)