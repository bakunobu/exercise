import math

# a
def calc_expr_one(e:float, f:float) -> float:
    a = (e + f / 2) / 3
    return(a)

# b
def calc_expr_two(h:float, g:float) -> float:
    b = abs(h ** 2 - g)
    return(b)

# c
def calc_expr_three(e:float,
                    g:float,
                    h:float) -> float:
    
    c = math.sqrt((g - h) ** 2 - 3 * math.sin(e))
    return(c)


