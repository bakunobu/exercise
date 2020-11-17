def solve_eq(a: float) -> float:
    expr_1 = a ** 2 + 10
    expr_2 = (a ** 2 + 1) ** 0.5
    y = expr_1 / expr_2
    return(y)


for a in (1, 0.3, 0, -2):
    print(solve_eq(a))    