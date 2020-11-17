import math

# a
def calc_eq_one(a:float, b:float) -> float:
    expr_1 = 2 / (a ** 2 + 25) + b
    expr_2 = math.sqrt(b) + (a + b) / 2
    try:
        x = expr_1/expr_2
        return(x)
    except ZeroDivisionError:
        print('Деление на 0')
        return(None)

# b 
def calc_eq_two(a:float, b:float) -> float:
    expr_1 = abs(a) + 2 * math.sin(b)
    expr_2 = 5.5 * a
    try:
        y = expr_1/expr_2
        return(y)
    except ZeroDivisionError:
        print('Деление на 0')
        return(None)
    