def luggage(a_1:float, a_2:float, a_3:float,
            b_1:float, b_2:float, b_3:float,) -> bool:
    l_1, l_2, l_3 = sorted((a_1, a_2, a_3))
    b_1, b_2, b_3 = sorted((b_1, b_2, b_3))
    return(b_1 < l_1 and b_2 < l_2 and b_3 < l_3)
    