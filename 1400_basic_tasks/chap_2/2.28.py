import math


def find_с(angle:int, b_h:float) -> float:
    c = math.cos(angle) * b_h
    return(c)

def find_trap_area(angle:int, b:float, c:float) -> float:
    S = c * math.sin(angle) * (b + c * math.cos(angle))
    return(S)

def main_func(a:float, b:float, angle:int) -> float:
    b_h = abs(a - b) / 2
    c = find_c(angle, b_h)
    S = find_trap_area(angle, b, c)
    
    