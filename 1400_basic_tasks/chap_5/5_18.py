def expr_one(a:float) -> float:
    return(3 * a)


def expr_two(a:float) -> float:
    t = expr_one(a)
    z = 4.3 * t ** 2 - 8 * t + 13
    return(z)


for x in range(2, 18):
    print(expr_two(x))