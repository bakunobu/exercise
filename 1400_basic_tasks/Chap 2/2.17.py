import math

def find_p_trap(a_1:float,
                a_2:float,
                h:float) -> float:
    a_h = abs(a_1 - a_2) / 2
    
    b = math.sqrt(h ** 2 + a_h ** 2)
    
    return(a_1 + a_2 + b * 2)