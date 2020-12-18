def substraction(a_1:int,
                 a_2:int,
                 a_3:int,
                 b_1:int,
                 b_2:int) -> tuple:
    if b_1 > a_1:
        a_2 -= 1
        a_1 += 10
    a_1 -= b_1
    
    if b_2 > a_2:
        a_3 -= 1
        a_2 += 10
    a_2 -= b_2
    
    return(a_3, a_2, a_1)        
        