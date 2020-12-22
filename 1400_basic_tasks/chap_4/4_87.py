def who_s_older(y_1:int, m_1:int, d_1:int,
                y_2:int, m_2:int, d_2:int) -> int:
    if y_1 > y_2:
        return(1)
    elif y_1 < y_2:
        return(2)
    
    if m_1 > m_2:
        return(1)
    elif m_1 < m_2:
        return(2)
    
    if d_1 > d_2:
        return(1)
    elif d_1 < d_2:
        return(2)
    
    return(0)