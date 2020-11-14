import math

def trap_perim(b:float, d:float, h:float) -> float:
    a = abs(b - d) / 2
    c = math.sqrt(a ** 2 + h ** 2)
    p = 2 * c + b + d
    return(p)

print(trap_perim(3, 4, 5))