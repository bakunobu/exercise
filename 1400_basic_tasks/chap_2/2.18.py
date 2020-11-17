import math

# a
def solve_eq_one(x: float, y: float) -> float:
    expr_1 = (2 + y) / x ** 2 + x
    expr_2a = math.sqrt(x ** 2 + 10)
    expr_2 = 1 / expr_2a + y
    return(expr_1 / expr_2)

# b
def solve_eq_two(x: float, y: float) -> float:
    expr = 7.25 * math.sin(x) - abs(y)
    return(expr)