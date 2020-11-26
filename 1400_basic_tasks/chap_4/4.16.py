import math



def solve_quad_eq(a:float,
                  b:float,
                  c:float) -> tuple:
    
    D = b ** 2 - 4 * a * c
    
    if D < 0:
        return(tuple('No'))
    elif D == 0:
        return(tuple(-b / (2 * a)))
    else:
        x_1 = (-b + math.sqrt(D)) / (2 * a)
        x_2 = (-b - math.sqrt(D)) / (2 * a)
        return(x_1, x_2)