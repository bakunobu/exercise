def substraction(a_1:int, a_2:int, b:int) -> tuple:
    if a_2 < b:
        a_2 -= 1
        a_1 += (10 - b)
    else:
        a_1 -= b
    return(a_2, a_1)