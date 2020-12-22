def time_dif(y_1:int, m_1:int,
             y:int=2020, m:int = 12) -> tuple:
    if m < m_1:
        y -= 1
        m += 12
    
    months = m - m_1
    years = y - y_1
    return(years, months)