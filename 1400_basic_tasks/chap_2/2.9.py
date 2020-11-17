# a
def calc_expr_one(x:float, y:float) -> float:
    expr_1 = 2 * x ** 3 - 3.44 * x * y
    expr_2 = 2.3 * x ** 2 - 7.1 * y + 2
    z = expr_1 + expr_2
    return(z)

print(calc_expr_one(1, 3))


# b
def calc_expr_two(a:float, b:float) -> float:
    expr_1 = 3.14 * (a + b) ** 3 + 2.75 * b ** 2
    expr_2 = 12.7 * a - 4.1
    x = expr_1 - expr_2
    return(x)

print(calc_expr_two(7, -2))