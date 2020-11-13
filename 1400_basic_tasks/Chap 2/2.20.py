import math

# a
def calc_eq_one(e:float,
                f:float,
                g:float) -> float:
    
    try:
        expr_1 = abs(e - 3 / f) ** 3
    except ZeroDivisionError:
        print('Деление на 0')
        return(None)
    
    a = math.sqrt(expr_1 + g)
    return(a)


# b
def calc_eq_two(e:float, h:float) -> float:
    expr_1 = math.sin(e)
    expr_2 = math.cos(h) ** 2
    return(expr_1 + expr_2)


# c
def calc_eq_three(e:float,
                  f:float,
                  g:float) -> float:
    expr_1 = 33 * g / (e * f - 3)
    return(expr_1)