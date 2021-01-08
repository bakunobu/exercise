def calc_expr_one(x:float) -> float:
    return(x + 3)


def calc_expr_two(x:float) -> float:
    t = calc_expr_one(x)
    y = 3 * t ** 2 + 4.87 * t - 3
    return(y)


for x in range(4, 29):
    print(calc_expr_two(x))